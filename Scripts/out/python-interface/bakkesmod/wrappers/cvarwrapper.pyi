from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class CVarWrapper():
    # Public:
    # CVarWrapper::CVarWrapper(uintptr_t mem, std::type_index pluginIdx) [constructor]
    def __init__(self, mem: int, pluginIdx: type_index) -> None: ...

    # CVarWrapper::CVarWrapper(CVarWrapper const & other) [constructor]

    # CVarWrapper & CVarWrapper::operator=(CVarWrapper rhs) [member operator]

    # CVarWrapper::~CVarWrapper() [destructor]
    def __del__(self) -> None: ...

    # std::string CVarWrapper::getCVarName() [member function]
    def getCVarName(self) -> str: ...

    # int CVarWrapper::getIntValue() [member function]
    def getIntValue(self) -> int: ...

    # float CVarWrapper::getFloatValue() [member function]
    def getFloatValue(self) -> float: ...

    # bool CVarWrapper::getBoolValue() [member function]
    def getBoolValue(self) -> bool: ...

    # LinearColor CVarWrapper::getColorValue() [member function]
    def getColorValue(self) -> LinearColor: ...

    # std::string CVarWrapper::getStringValue() [member function]
    def getStringValue(self) -> str: ...

    # std::string CVarWrapper::getDescription() [member function]
    def getDescription(self) -> str: ...

    # std::string const CVarWrapper::GetDefaultValue() [member function]
    def GetDefaultValue(self) -> str: ...

    # bool CVarWrapper::HasMinimum() [member function]
    def HasMinimum(self) -> bool: ...

    # bool CVarWrapper::HasMaximum() [member function]
    def HasMaximum(self) -> bool: ...

    # float CVarWrapper::GetMinimum() [member function]
    def GetMinimum(self) -> float: ...

    # float CVarWrapper::GetMaximum() [member function]
    def GetMaximum(self) -> float: ...

    # bool CVarWrapper::IsHidden() [member function]
    def IsHidden(self) -> bool: ...

    # bool CVarWrapper::ShouldSaveToCfg() [member function]
    def ShouldSaveToCfg(self) -> bool: ...

    # void CVarWrapper::ResetToDefault() [member function]
    def ResetToDefault(self) -> None: ...

    # void CVarWrapper::notify() [member function]
    def notify(self) -> None: ...

    # void CVarWrapper::setValue(std::string value) [member function]
    def setValue(self, value: str) -> None: ...

    # void CVarWrapper::setValue(int value) [member function]
    def setValue(self, value: int) -> None: ...

    # void CVarWrapper::setValue(float value) [member function]
    def setValue(self, value: float) -> None: ...

    # void CVarWrapper::setValue(LinearColor value) [member function]
    def setValue(self, value: LinearColor) -> None: ...

    # void CVarWrapper::addOnValueChanged(std::function<void (std::basic_string<char>, CVarWrapper)> changeFunc) [member function]
    def addOnValueChanged(self, changeFunc: Callable[[str, CVarWrapper], None]) -> None: ...

    # void CVarWrapper::removeOnValueChanged() [member function]
    def removeOnValueChanged(self) -> None: ...

    # void CVarWrapper::bindTo(std::shared_ptr<int> var) [member function]
    def bindTo(self, var: int) -> None: ...

    # void CVarWrapper::bindTo(std::shared_ptr<float> var) [member function]
    def bindTo(self, var: float) -> None: ...

    # void CVarWrapper::bindTo(std::shared_ptr<std::basic_string<char> > var) [member function]
    def bindTo(self, var: str) -> None: ...

    # void CVarWrapper::bindTo(std::shared_ptr<bool> var) [member function]
    def bindTo(self, var: bool) -> None: ...

    # void CVarWrapper::bindTo(std::shared_ptr<LinearColor> var) [member function]
    def bindTo(self, var: LinearColor) -> None: ...

    # bool CVarWrapper::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # bool CVarWrapper::operator bool() [casting operator]

    # Private:
    # CVarWrapper::Impl [class declaration]

    # CVarWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


