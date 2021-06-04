from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class AIControllerWrapper():
    # Public:
    # AIControllerWrapper::AIControllerWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # AIControllerWrapper::AIControllerWrapper(AIControllerWrapper const & other) [constructor]

    # AIControllerWrapper & AIControllerWrapper::operator=(AIControllerWrapper rhs) [member operator]

    # AIControllerWrapper::~AIControllerWrapper() [destructor]
    def __del__(self) -> None: ...

    # void AIControllerWrapper::DoNothing() [member function]
    def DoNothing(self) -> None: ...

    # Private:
    # AIControllerWrapper::Impl [class declaration]

    # AIControllerWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


