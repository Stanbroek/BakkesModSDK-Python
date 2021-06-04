from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class CVarManagerWrapper():
    # Public:
    # CVarManagerWrapper::CVarManagerWrapper(uintptr_t mem, std::type_index pluginIdx) [constructor]
    def __init__(self, mem: int, pluginIdx: type_index) -> None: ...

    # CVarManagerWrapper::CVarManagerWrapper(CVarManagerWrapper const & other) [constructor]

    # CVarManagerWrapper & CVarManagerWrapper::operator=(CVarManagerWrapper rhs) [member operator]

    # CVarManagerWrapper::~CVarManagerWrapper() [destructor]
    def __del__(self) -> None: ...

    # void CVarManagerWrapper::executeCommand(std::string command, bool log=true) [member function]
    def executeCommand(self, command: str, log: bool = True) -> None: ...

    # void CVarManagerWrapper::registerNotifier(std::string cvar, commandNotifier notifier, std::string description, unsigned char permissions) [member function]
    def registerNotifier(self, cvar: str, notifier: Callable[[List[str]], None], description: str, permissions: int) -> None: ...

    # void CVarManagerWrapper::registerNotifier(std::string cvar, std::function<void (std::vector<std::basic_string<char>, std::allocator<std::basic_string<char> > >)> notifier, std::string description, unsigned char permissions) [member function]
    def registerNotifier(self, cvar: str, notifier: Callable[[List[str]], None], description: str, permissions: int) -> None: ...

    # bool CVarManagerWrapper::removeNotifier(std::string cvar) [member function]
    def removeNotifier(self, cvar: str) -> bool: ...

    # CVarWrapper CVarManagerWrapper::registerCvar(std::string cvar, std::string defaultValue, std::string desc="", bool searchAble=true, bool hasMin=false, float min=0, bool hasMax=false, float max=0, bool saveToCfg=true) [member function]
    def registerCvar(self, cvar: str, defaultValue: str, desc: str = "", searchAble: bool = True, hasMin: bool = False, min: float = 0, hasMax: bool = False, max: float = 0, saveToCfg: bool = True) -> CVarWrapper: ...

    # bool CVarManagerWrapper::removeCvar(std::string cvar) [member function]
    def removeCvar(self, cvar: str) -> bool: ...

    # void CVarManagerWrapper::log(std::string text) [member function]
    def log(self, text: str) -> None: ...

    # void CVarManagerWrapper::log(std::wstring text) [member function]
    def log(self, text: str) -> None: ...

    # CVarWrapper CVarManagerWrapper::getCvar(std::string cvar) [member function]
    def getCvar(self, cvar: str) -> CVarWrapper: ...

    # std::string CVarManagerWrapper::getBindStringForKey(std::string key) [member function]
    def getBindStringForKey(self, key: str) -> str: ...

    # void CVarManagerWrapper::setBind(std::string key, std::string command) [member function]
    def setBind(self, key: str, command: str) -> None: ...

    # void CVarManagerWrapper::removeBind(std::string key) [member function]
    def removeBind(self, key: str) -> None: ...

    # std::string CVarManagerWrapper::getAlias(std::string alias) [member function]
    def getAlias(self, alias: str) -> str: ...

    # void CVarManagerWrapper::setAlias(std::string key, std::string script) [member function]
    def setAlias(self, key: str, script: str) -> None: ...

    # void CVarManagerWrapper::backupCfg(std::string path) [member function]
    def backupCfg(self, path: str) -> None: ...

    # void CVarManagerWrapper::backupBinds(std::string path) [member function]
    def backupBinds(self, path: str) -> None: ...

    # void CVarManagerWrapper::loadCfg(std::string path) [member function]
    def loadCfg(self, path: str) -> None: ...

    # Private:
    # CVarManagerWrapper::Impl [class declaration]

    # CVarManagerWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


