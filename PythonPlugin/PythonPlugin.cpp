#include "PythonPlugin.h"

BAKKESMOD_PLUGIN(PythonPlugin, "PythonPlugin", PLUGIN_VERSION, PLUGINTYPE_ALL)

std::filesystem::path BakkesModCrashesFolder;

std::shared_ptr<int> LogLevel;
std::shared_ptr<CVarManagerWrapperDebug> GlobalCVarManager;


std::vector<std::filesystem::path> getPythonFilesFromPath(const std::filesystem::path& path)
{
    std::vector<std::filesystem::path> files;
    for (const std::filesystem::directory_entry& file : std::filesystem::directory_iterator(path)) {
        const std::filesystem::path& filePath = file.path();
        if (file.is_regular_file() && filePath.extension() == L".py") {
            files.push_back(filePath);
        }
    }

    return files;
}


void PythonPlugin::UnloadAll()
{
    TRACE_LOG("Unload all");
    if (loadedPlugins.empty()) {
        TRACE_LOG("No plugins loaded");
        return;
    }

    for (const auto& [loadedPlugin, _] : loadedPlugins) {
        UnloadPlugin(loadedPlugin);
    }
}


void PythonPlugin::ReloadAll()
{
    TRACE_LOG("Reload all");
    if (loadedPlugins.empty()) {
        TRACE_LOG("No plugins loaded");
        return;
    }

    for (const auto& [loadedPlugin, _] : loadedPlugins) {
        ReloadPlugin(loadedPlugin);
    }
}


void PythonPlugin::ListPlugins() const
{
    TRACE_LOG("List all");
    const std::vector<std::filesystem::path>& files = getPythonFilesFromPath(pythonPluginFolder);
    if (files.empty()) {
        ERROR_LOG("Could not find any plugins");
        return;
    }

    for (const std::filesystem::path& file : files) {
        LOG("{}", file.filename().u8string());
    }
}


void PythonPlugin::LoadPlugin(const std::string& plugin)
{
    TRACE_LOG("loading {}", plugin);
    if (loadedPlugins.find(to_lower(plugin)) != loadedPlugins.end()) {
        ERROR_LOG("{} is already loaded", plugin);
        return;
    }
    
    const std::shared_ptr<LoadedPlugin> loadedPlugin = std::make_shared<LoadedPlugin>(pythonPluginFolder / plugin);
    logStream(plugin);
    if (pybind11::hasattr(loadedPlugin->Module, "onLoad")) {
        CATCH_PYTHON_EXCEPTIONS(loadedPlugin->Module.attr("onLoad")(););
        logStream(plugin);
    }
    else {
        WARNING_LOG("{} does not have a onLoad function", plugin);
    }
    loadedPlugins.emplace(to_lower(plugin), loadedPlugin);
}


void PythonPlugin::UnloadPlugin(const std::string& plugin)
{
    TRACE_LOG("unloading {}", plugin);
    if (loadedPlugins.find(to_lower(plugin)) == loadedPlugins.end()) {
        ERROR_LOG("{} is not loaded", plugin);
        return;
    }
    
    const std::shared_ptr<LoadedPlugin>& loadedPlugin = loadedPlugins[to_lower(plugin)];
    if (pybind11::hasattr(loadedPlugin->Module, "onUnload")) {
        LOG_PYTHON_EXCEPTIONS(loadedPlugin->Module.attr("onUnload")(););
        logStream(plugin);
    }
    else {
        WARNING_LOG("{} does not have a onUnload function", plugin);
    }
    loadedPlugins.erase(to_lower(plugin));
    logStream(plugin);
}


void PythonPlugin::ReloadPlugin(const std::string& plugin)
{
    TRACE_LOG("reload {}", plugin);
    if (loadedPlugins.find(to_lower(plugin)) == loadedPlugins.end()) {
        ERROR_LOG("{} is not loaded", plugin);
        return;
    }

    UnloadPlugin(plugin);
    LoadPlugin(plugin);
}


void PythonPlugin::EnsurePlugin(const std::string& plugin)
{
    TRACE_LOG("ensure {}", plugin);
    if (loadedPlugins.find(to_lower(plugin)) != loadedPlugins.end()) {
        UnloadPlugin(plugin);
    }

    LoadPlugin(plugin);
}


/// <summary>Logs pythons stdout and stderr buffers to BakkesMod.</summary>
/// <param name="pluginName">Name of the plugin that filled the buffers.</param>
void PythonPlugin::logStream(const std::string& pluginName)
{
    std::stringstream stdoutStream(streamRedirect.stdoutString());
    if (stdoutStream && stdoutStream.rdbuf()->in_avail()) {
        std::string line;
        while (std::getline(stdoutStream, line, '\n')) {
            LOG("[{}] {}", pluginName, line);
        }
    }

    std::stringstream stderrStream(streamRedirect.stderrString());
    if (stderrStream && stderrStream.rdbuf()->in_avail()) {
        std::string line;
        while (std::getline(stderrStream, line, '\n')) {
            ERROR_LOG("[{}] {}", pluginName, line);
        }
    }
}


/// <summary>Registers notifiers and variables to interact with the plugin on load.</summary>
void PythonPlugin::OnLoad()
{
    BakkesModCrashesFolder = gameWrapper->GetBakkesModPath() / L"crashes";
    if (!exists(BakkesModCrashesFolder)) {
        std::filesystem::create_directory(BakkesModCrashesFolder);
    }

    // Copy the original cvarManager so we can use it everywhere.
    GlobalCVarManager = std::reinterpret_pointer_cast<CVarManagerWrapperDebug>(cvarManager);

    // Initialize BakkesMod bindings.
    LOG_PYTHON_EXCEPTIONS(
        const pybind11::module bmModule = pybind11::module::import("bakkesmod");
        bmModule.attr("cvarManager") = cvarManager;
        bmModule.attr("gameWrapper") = gameWrapper;
    );

    /* Register CVars */
    cvarManager->registerCvar("pp_plugin_dir", "", "Python plugins path", true, false, 0, false, 0, true);
    cvarManager->getCvar("pp_plugin_dir").addOnValueChanged([this](const std::string&, CVarWrapper cvar) {
        pythonPluginFolder = cvar.getStringValue();
        pybind11::module::import("sys").attr("path").cast<pybind11::list>().append(std::filesystem::absolute(pythonPluginFolder).string());
    });
    cvarManager->getCvar("pp_plugin_dir").setValue(std::filesystem::absolute(gameWrapper->GetBakkesModPath() / "py").string());

    LogLevel = std::make_shared<int>(0);
    cvarManager->registerCvar("pp_log_level", std::to_string(CVarManagerWrapperDebug::level_enum::normal),
        "Log level", true, false, 0, false, 0, false).bindTo(LogLevel);

#ifdef DEBUG
    cvarManager->getCvar("pp_log_level").setValue(CVarManagerWrapperDebug::level_enum::all);
#endif

    /* Register Notifiers */
    RegisterNotifier("pplugin", [this](const std::vector<std::string>& arguments) {
        if (arguments.size() < 2) {
            LOG("Usage: pplugin reloadall|unloadall|list|load|unload|reload|ensure [pluginname]");
            return;
        }

        const std::string command = arguments[1];
        if (command == "unloadall") {
            UnloadAll();
            return;
        }
        if (command == "reloadall") {
            ReloadAll();
            return;
        }
        if (command == "list") {
            ListPlugins();
            return;
        }

        if (arguments.size() > 2) {
            const std::string pluginName = arguments[2];
            if (command == "load") {
                LoadPlugin(pluginName);
                return;
            }
            if (command == "unload") {
                UnloadPlugin(pluginName);
                return;
            }
            if (command == "reload") {
                ReloadPlugin(pluginName);
                return;
            }
            if (command == "ensure") {
                EnsurePlugin(pluginName);
                return;
            }
        }

        LOG("Usage: pplugin reloadall|unloadall|list|load|unload|reload|ensure [pluginname]");
    }, "load/unload/reload/list python plugins, usage: pplugin reloadall|unloadall|list|load|unload|reload|ensure [pluginname]", PERMISSION_ALL);
    
    RegisterNotifier("pp_list_loaded_plugins", [this](const std::vector<std::string>&) {
        if (loadedPlugins.empty()) {
            LOG("No plugins are loaded");
        }
        for (const auto& [name, loadedPlugin] : loadedPlugins) {
            LOG(name);
        }
    }, "Lists loaded python plugins", PERMISSION_ALL);

    RegisterNotifier("pp_refresh_cache", [this](const std::vector<std::string>&) {
        std::string pluginName = std::filesystem::path(exports.fileName).stem().string();
        cvarManager->executeCommand("sleep 0; plugin unload " + pluginName);
        LOG("Refreshing cache");
        cvarManager->executeCommand("sleep 1; plugin load " + pluginName);
    }, "Refreshes python cache", PERMISSION_ALL);

    /* Register Hooks */
    HookEventWithCaller<ActorWrapper>("Function Engine.GameViewportClient.Tick",
        [this](const ActorWrapper&, void*, const std::string&) {
            logStream("Global");
        });
}


/// <summary>Unload the plugin properly.</summary>
void PythonPlugin::OnUnload()
{
    UnloadAll();
}
