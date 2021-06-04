from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SequenceObjectWrapper():
    # Public:
    # SequenceObjectWrapper::SequenceObjectWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # SequenceObjectWrapper::SequenceObjectWrapper(SequenceObjectWrapper const & other) [constructor]

    # SequenceObjectWrapper & SequenceObjectWrapper::operator=(SequenceObjectWrapper rhs) [member operator]

    # SequenceObjectWrapper::~SequenceObjectWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool SequenceObjectWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool SequenceObjectWrapper::operator bool() const [casting operator]

    # SequenceWrapper SequenceObjectWrapper::GetParentSequence() [member function]
    def GetParentSequence(self) -> SequenceWrapper: ...

    # UnrealStringWrapper SequenceObjectWrapper::GetObjName() [member function]
    def GetObjName(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper SequenceObjectWrapper::GetObjCategory() [member function]
    def GetObjCategory(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper SequenceObjectWrapper::GetObjComment() [member function]
    def GetObjComment(self) -> UnrealStringWrapper: ...

    # Private:
    # SequenceObjectWrapper::Impl [class declaration]

    # SequenceObjectWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


