from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class FormField():
    # Public:
    # FormField::Type [enumeration]
    class Type(Enum):
        kString = 0
        kFile = 1

    # FormField::field_type [variable]
    @property
    def field_type(self) -> Type: ...

    # FormField::data [variable]
    @property
    def data(self) -> str: ...

    # FormField::name [variable]
    @property
    def name(self) -> str: ...

    # FormField::FormField(FormField const & arg0) [constructor]

    # FormField::~FormField() [destructor]
    def __del__(self) -> None: ...

    # FormField::FormField() [constructor]
    def __init__(self) -> None: ...

    # FormField & FormField::operator=(FormField const & arg0) [member operator]


class CurlRequest():
    # Public:
    # CurlRequest::url [variable]
    @property
    def url(self) -> str: ...

    # CurlRequest::verb [variable]
    @property
    def verb(self) -> str: ...

    # CurlRequest::headers [variable]
    @property
    def headers(self) -> Dict[str, str]: ...

    # CurlRequest::body [variable]
    @property
    def body(self) -> str: ...

    # CurlRequest::form_data [variable]
    @property
    def form_data(self) -> List[FormField]: ...

    # CurlRequest::progress_function [variable]
    @property
    def progress_function(self) -> Callable[[float, float, float, float], None]: ...

    # CurlRequest::CurlRequest(CurlRequest const & arg0) [constructor]

    # CurlRequest::~CurlRequest() [destructor]
    def __del__(self) -> None: ...

    # CurlRequest::CurlRequest() [constructor]
    def __init__(self) -> None: ...

    # CurlRequest & CurlRequest::operator=(CurlRequest const & arg0) [member operator]


