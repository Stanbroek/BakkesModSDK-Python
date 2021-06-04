/// pch.h: This is a precompiled header file.
/// Files listed below are compiled only once, improving build performance for future builds.
/// This also affects IntelliSense performance, including code completion and many code browsing features.
/// However, files listed here are ALL re-compiled if any one of them is updated between builds.
/// Do not add files here that you will be updating frequently as this negates the performance advantage.

#ifndef PCH_H
#define PCH_H

/// add headers that you want to pre-compile here
#define WIN32_LEAN_AND_MEAN            // Exclude rarely-used stuff from Windows headers
#define NOMINMAX
#define CATCH_PYTHON_EXCEPTIONS(code)       \
    try {                                   \
        code                                \
    }                                       \
    catch (const std::runtime_error& e) {   \
        CRITICAL_LOG(e.what());             \
        return;                             \
    }
#define LOG_PYTHON_EXCEPTIONS(code)         \
    try {                                   \
        code                                \
    }                                       \
    catch (const std::runtime_error& e) {   \
        CRITICAL_LOG(e.what());             \
    }

// Windows Headers
#include <Windows.h>
#include <string>
#include <vector>

// BakkesMod SDK
#pragma comment( lib, "pluginsdk.lib" )
#pragma warning(push, 0)
#include "bakkesmod/plugin/bakkesmodplugin.h"
#include "bakkesmod/plugin/pluginwindow.h"

// Include everything
#include "bakkesmod/wrappers/includes.h"
// and even more
#include "bakkesmod/wrappers/Engine/WorldInfoWrapper.h"
#include "bakkesmod/wrappers/GameObject/RumbleComponent/BasketballPickup.h"
#include "bakkesmod/wrappers/GameObject/PerformanceStats/StartGraphSystemWrapper.h"
#include "bakkesmod/wrappers/GameObject/Stats/StatEventWrapper.h"
#include "bakkesmod/wrappers/kismet/SequenceVariableWrapper.h"
#include "bakkesmod/wrappers/kismet/SequenceWrapper.h"
#include "bakkesmod/wrappers/PluginManagerWrapper.h"
//#include "bakkesmod/wrappers/replaywrapper.h"
#pragma warning(pop)

// BakkesMod SDK Additions
#include "utils/cvarmanagerwrapperdebug.h"
#include "utils/exception_safety.h"

enum {
    PLUGINTYPE_ALL = 0x00
};

// General Utils
#include "utils/stringify.h"

// pybind11
#include "pybind11/pybind11.h"
#include "pybind11/functional.h"
#include "pybind11/operators.h"
#include "pybind11/stl.h"
#include "pybind11/embed.h"

#endif //PCH_H
