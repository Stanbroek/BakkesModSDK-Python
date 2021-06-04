from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class TextInputModalWrapper():
    # Public:
    # TextInputModalWrapper::TextInputModalWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # TextInputModalWrapper::TextInputModalWrapper(TextInputModalWrapper const & other) [constructor]

    # TextInputModalWrapper & TextInputModalWrapper::operator=(TextInputModalWrapper rhs) [member operator]

    # TextInputModalWrapper::~TextInputModalWrapper() [destructor]
    def __del__(self) -> None: ...

    # void TextInputModalWrapper::SetTextInput(std::string const & defaultText, int32_t max_text_length, bool password, std::function<void (std::basic_string<char>, bool)> input_callback) [member function]
    def SetTextInput(self, defaultText: str, max_text_length: int32_t, password: bool, input_callback: Callable[[str, bool], None]) -> None: ...

    # Private:
    # TextInputModalWrapper::Impl [class declaration]

    # TextInputModalWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


