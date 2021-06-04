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


class PyStdErrOutStreamRedirect
{
public:
    PyStdErrOutStreamRedirect()
    {
        const pybind11::module sysm = pybind11::module::import("sys");
        _stdout = sysm.attr("stdout");
        _stderr = sysm.attr("stderr");
        const auto stringIO = pybind11::module::import("io").attr("StringIO");
        _stdout_buffer = stringIO();  // Other filelike object can be used here as well, such as objects created by pybind11
        _stderr_buffer = stringIO();
        sysm.attr("stdout") = _stdout_buffer;
        sysm.attr("stderr") = _stderr_buffer;
    }

    std::string stdoutString() const
    {
        _stdout_buffer.attr("seek")(0);
        const std::string buffer = pybind11::str(_stdout_buffer.attr("read")());
        if (!buffer.empty()) {
            _stdout_buffer.attr("seek")(_stdout_buffer.attr("truncate")(0));
        }

        return buffer;
    }

    std::string stderrString() const
    {
        _stderr_buffer.attr("seek")(0);
        const std::string buffer = pybind11::str(_stderr_buffer.attr("read")());
        if (!buffer.empty()) {
            _stderr_buffer.attr("seek")(_stderr_buffer.attr("truncate")(0));
        }

        return buffer;
    }

    ~PyStdErrOutStreamRedirect()
    {
        const pybind11::module sysm = pybind11::module::import("sys");
        _stdout_buffer.attr("close")();
        sysm.attr("stdout") = _stdout;
        _stderr_buffer.attr("close")();
        sysm.attr("stderr") = _stderr;
    }

private:
    pybind11::object _stdout;
    pybind11::object _stderr;
    pybind11::object _stdout_buffer;
    pybind11::object _stderr_buffer;
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
    PyStdErrOutStreamRedirect streamRedirect;

    void logStream(const std::string& pluginName);

    /* BakkesMod Plugin Overrides */
public:
    CATCH_DEFAULT_BM_FUNCTIONS;
private:
};
