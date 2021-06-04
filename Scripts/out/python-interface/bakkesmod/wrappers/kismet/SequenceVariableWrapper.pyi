from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SequenceVariableWrapper():
    # Public:
    # SequenceVariableWrapper::SequenceVariableWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # SequenceVariableWrapper::SequenceVariableWrapper(SequenceVariableWrapper const & other) [constructor]

    # SequenceVariableWrapper & SequenceVariableWrapper::operator=(SequenceVariableWrapper rhs) [member operator]

    # SequenceVariableWrapper::~SequenceVariableWrapper() [destructor]
    def __del__(self) -> None: ...

    # std::string SequenceVariableWrapper::GetVarName() [member function]
    def GetVarName(self) -> str: ...

    # bool SequenceVariableWrapper::IsInt() [member function]
    def IsInt(self) -> bool: ...

    # bool SequenceVariableWrapper::IsFloat() [member function]
    def IsFloat(self) -> bool: ...

    # bool SequenceVariableWrapper::IsString() [member function]
    def IsString(self) -> bool: ...

    # bool SequenceVariableWrapper::IsVector() [member function]
    def IsVector(self) -> bool: ...

    # bool SequenceVariableWrapper::IsBool() [member function]
    def IsBool(self) -> bool: ...

    # bool SequenceVariableWrapper::IsObjectList() [member function]
    def IsObjectList(self) -> bool: ...

    # bool SequenceVariableWrapper::IsActor() [member function]
    def IsActor(self) -> bool: ...

    # float SequenceVariableWrapper::GetFloat() [member function]
    def GetFloat(self) -> float: ...

    # int SequenceVariableWrapper::GetInt() [member function]
    def GetInt(self) -> int: ...

    # std::string SequenceVariableWrapper::GetString() [member function]
    def GetString(self) -> str: ...

    # Vector SequenceVariableWrapper::GetVector() [member function]
    def GetVector(self) -> Vector: ...

    # bool SequenceVariableWrapper::GetBool() [member function]
    def GetBool(self) -> bool: ...

    # ArrayWrapper<SequenceVariableWrapper> SequenceVariableWrapper::GetObjectList() [member function]
    def GetObjectList(self) -> ArrayWrapper_SequenceVariableWrapper: ...

    # void SequenceVariableWrapper::SetFloat(float value) [member function]
    def SetFloat(self, value: float) -> None: ...

    # void SequenceVariableWrapper::SetInt(int value) [member function]
    def SetInt(self, value: int) -> None: ...

    # void SequenceVariableWrapper::SetString(std::string const & value) [member function]
    def SetString(self, value: str) -> None: ...

    # void SequenceVariableWrapper::SetVector(Vector value) [member function]
    def SetVector(self, value: Vector) -> None: ...

    # void SequenceVariableWrapper::SetBool(bool value) [member function]
    def SetBool(self, value: bool) -> None: ...

    # ActorWrapper SequenceVariableWrapper::GetActor() [member function]
    def GetActor(self) -> ActorWrapper: ...

    # Private:
    # SequenceVariableWrapper::Impl [class declaration]

    # SequenceVariableWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


