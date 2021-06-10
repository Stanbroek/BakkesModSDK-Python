#pragma once
#include "Version.h"

constexpr const char* PLUGIN_VERSION = VER_FILE_VERSION_STR;


struct LoadedPlugin
{
    std::string Name;
    std::filesystem::path Path;
    pybind11::module Module;

    LoadedPlugin(const std::filesystem::path& path) : Path(path)
    {
        Name = path.stem().string();
        const pybind11::dict modules = pybind11::module::import("sys").attr("modules");
        if (modules.contains(Name)) {
            TRACE_LOG("Reloading {}", Name);
            Module = modules[Name.c_str()];
            Module.reload();
        }
        else {
            TRACE_LOG("Importing {}", Name);
            Module = pybind11::module::import(Name.c_str());
        }
    }

    LoadedPlugin(const LoadedPlugin&) = delete;
    LoadedPlugin(LoadedPlugin&&) = delete;
    LoadedPlugin& operator=(const LoadedPlugin&) = delete;
    LoadedPlugin& operator=(LoadedPlugin&&) = delete;
};


class PythonPlugin final: public BakkesMod::Plugin::BakkesModPlugin
{
public:
    void UnloadAll();
    void ReloadAll();
    void ListPlugins() const;

    void LoadPlugin(const std::string& plugin);
    void UnloadPlugin(const std::string& plugin);
    void ReloadPlugin(const std::string& plugin);
    void EnsurePlugin(const std::string& plugin);

private:
    std::filesystem::path pythonPluginFolder;
    std::map<std::string, std::shared_ptr<LoadedPlugin>> loadedPlugins;

    pybind11::scoped_interpreter interpreter;

    /* BakkesMod Plugin Overrides */
public:
    CATCH_DEFAULT_BM_FUNCTIONS;
private:
};
