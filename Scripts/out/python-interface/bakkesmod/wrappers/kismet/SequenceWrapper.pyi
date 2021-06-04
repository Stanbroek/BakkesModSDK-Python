from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SequenceWrapper():
    # Public:
    # SequenceWrapper::SequenceWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # SequenceWrapper::SequenceWrapper(SequenceWrapper const & other) [constructor]

    # SequenceWrapper & SequenceWrapper::operator=(SequenceWrapper rhs) [member operator]

    # SequenceWrapper::~SequenceWrapper() [destructor]
    def __del__(self) -> None: ...

    # ArrayWrapper<SequenceObjectWrapper> SequenceWrapper::GetSequenceObjects() [member function]
    def GetSequenceObjects(self) -> ArrayWrapper_SequenceObjectWrapper: ...

    # ArrayWrapper<SequenceWrapper> SequenceWrapper::GetNestedSequences() [member function]
    def GetNestedSequences(self) -> ArrayWrapper_SequenceWrapper: ...

    # int SequenceWrapper::ActivateRemoteEvents(std::string const & remote_event_name) const [member function]
    def ActivateRemoteEvents(self, remote_event_name: str) -> int: ...

    # std::map<std::basic_string<char>, SequenceVariableWrapper, std::less<std::basic_string<char> >, std::allocator<std::pair<const std::basic_string<char>, SequenceVariableWrapper> > > SequenceWrapper::GetAllSequenceVariables(bool reqursive) [member function]
    def GetAllSequenceVariables(self, reqursive: bool) -> Dict[str, SequenceVariableWrapper]: ...

    # Private:
    # SequenceWrapper::Impl [class declaration]

    # SequenceWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


