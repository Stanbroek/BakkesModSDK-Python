from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ImageWrapper():
    # Public:
    # ImageWrapper::ImageWrapper(std::string path, bool canvasLoad=false, bool ImGuiLoad=false) [constructor]
    def __init__(self, path: str, canvasLoad: bool = False, ImGuiLoad: bool = False) -> None: ...

    # ImageWrapper::ImageWrapper(std::wstring path, bool canvasLoad=false, bool ImGuiLoad=false) [constructor]
    def __init__(self, path: str, canvasLoad: bool = False, ImGuiLoad: bool = False) -> None: ...

    # ImageWrapper::~ImageWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool ImageWrapper::LoadForCanvas() [member function]
    def LoadForCanvas(self) -> bool: ...

    # bool ImageWrapper::IsLoadedForCanvas() [member function]
    def IsLoadedForCanvas(self) -> bool: ...

    # void * ImageWrapper::GetCanvasTex() [member function]
    def GetCanvasTex(self) -> Any: ...

    # void ImageWrapper::LoadForImGui(std::function<void (bool)> onLoaded) [member function]
    def LoadForImGui(self, onLoaded: Callable[[bool], None]) -> None: ...

    # bool ImageWrapper::IsLoadedForImGui() [member function]
    def IsLoadedForImGui(self) -> bool: ...

    # void * ImageWrapper::GetImGuiTex() [member function]
    def GetImGuiTex(self) -> Any: ...

    # std::string ImageWrapper::GetPath() [member function]
    def GetPath(self) -> str: ...

    # std::wstring ImageWrapper::GetPathW() [member function]
    def GetPathW(self) -> str: ...

    # Vector2 ImageWrapper::GetSize() [member function]
    def GetSize(self) -> Vector2: ...

    # Vector2F ImageWrapper::GetSizeF() [member function]
    def GetSizeF(self) -> Vector2F: ...

    # Private:
    # ImageWrapper::Impl [class declaration]

    # ImageWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


