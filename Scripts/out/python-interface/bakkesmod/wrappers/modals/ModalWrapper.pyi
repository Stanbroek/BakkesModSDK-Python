from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ModalWrapper():
    # Public:
    # ModalWrapper::ModalWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ModalWrapper::ModalWrapper(ModalWrapper const & other) [constructor]

    # ModalWrapper & ModalWrapper::operator=(ModalWrapper rhs) [member operator]

    # ModalWrapper::~ModalWrapper() [destructor]
    def __del__(self) -> None: ...

    # void ModalWrapper::ShowModal() const [member function]
    def ShowModal(self) -> None: ...

    # void ModalWrapper::CloseModal() [member function]
    def CloseModal(self) -> None: ...

    # void ModalWrapper::SetColor(float r, float g, float b) [member function]
    def SetColor(self, r: float, g: float, b: float) -> None: ...

    # void ModalWrapper::SetIcon(std::string const & iconName) [member function]
    def SetIcon(self, iconName: str) -> None: ...

    # void ModalWrapper::SetBody(std::string const & bodyHtml) [member function]
    def SetBody(self, bodyHtml: str) -> None: ...

    # void ModalWrapper::AddButton(std::string const & button_text, bool is_cancel_button, std::function<void ()> click_callback=nullptr) [member function]
    def AddButton(self, button_text: str, is_cancel_button: bool, click_callback: Callable[[], None] = None) -> None: ...

    # Private:
    # ModalWrapper::Impl [class declaration]

    # ModalWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


