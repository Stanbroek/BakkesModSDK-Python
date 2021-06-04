from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ObjectWrapper():
    # Public:
    # ObjectWrapper::memory_address [variable]
    @property
    def memory_address(self) -> int: ...

    # ObjectWrapper::ObjectWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ObjectWrapper::ObjectWrapper(ObjectWrapper const & arg0) [constructor]

    # ObjectWrapper & ObjectWrapper::operator=(ObjectWrapper const & arg0) [member operator]

    # ObjectWrapper::~ObjectWrapper() [destructor]
    def __del__(self) -> None: ...


