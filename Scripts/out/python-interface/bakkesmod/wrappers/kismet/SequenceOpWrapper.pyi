from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SequenceOpWrapper():
    # Public:
    # SequenceOpWrapper::SequenceOpWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # SequenceOpWrapper::SequenceOpWrapper(SequenceOpWrapper const & other) [constructor]

    # SequenceOpWrapper & SequenceOpWrapper::operator=(SequenceOpWrapper rhs) [member operator]

    # SequenceOpWrapper::~SequenceOpWrapper() [destructor]
    def __del__(self) -> None: ...

    # Private:
    # SequenceOpWrapper::Impl [class declaration]

    # SequenceOpWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


