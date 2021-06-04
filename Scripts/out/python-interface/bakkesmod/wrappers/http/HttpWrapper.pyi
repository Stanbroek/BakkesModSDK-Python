from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class HttpWrapper():
    # Public:
    # static void HttpWrapper::SendCurlRequest(CurlRequest request_data, CurlRequestDoneStringReturn on_complete) [member function]
    def SendCurlRequest(self, request_data: CurlRequest, on_complete: Callable[[int, str], None]) -> None: ...

    # static void HttpWrapper::SendCurlRequest(CurlRequest request_data, CurlRequestDoneBinaryReturn on_complete) [member function]
    def SendCurlRequest(self, request_data: CurlRequest, on_complete: Callable[[int, str, int], None]) -> None: ...

    # static void HttpWrapper::SendCurlRequest(CurlRequest request_data, std::wstring const & file_output, CurlRequestDoneFileReturn on_complete) [member function]
    def SendCurlRequest(self, request_data: CurlRequest, file_output: str, on_complete: Callable[[int, str], None]) -> None: ...

    # static void HttpWrapper::SendCurlJsonRequest(CurlRequest request_data, CurlRequestDoneStringReturn on_complete) [member function]
    def SendCurlJsonRequest(self, request_data: CurlRequest, on_complete: Callable[[int, str], None]) -> None: ...

    # HttpWrapper::HttpWrapper() [constructor]
    def __init__(self) -> None: ...

    # HttpWrapper::HttpWrapper(HttpWrapper const & arg0) [constructor]

    # HttpWrapper & HttpWrapper::operator=(HttpWrapper const & arg0) [member operator]

    # HttpWrapper::~HttpWrapper() [destructor]
    def __del__(self) -> None: ...


