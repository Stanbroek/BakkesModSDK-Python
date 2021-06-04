from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class AttachmentPickup():
    # Public:
    # AttachmentPickup::AttachmentPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # AttachmentPickup::AttachmentPickup(AttachmentPickup const & other) [constructor]

    # AttachmentPickup & AttachmentPickup::operator=(AttachmentPickup rhs) [member operator]

    # AttachmentPickup::~AttachmentPickup() [destructor]
    def __del__(self) -> None: ...

    # void AttachmentPickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void AttachmentPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # AttachmentPickup::Impl [class declaration]

    # AttachmentPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


