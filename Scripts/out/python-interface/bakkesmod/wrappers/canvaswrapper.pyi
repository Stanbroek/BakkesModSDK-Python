from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class CanvasWrapper():
    # Public:
    # CanvasWrapper::CanvasWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # CanvasWrapper::CanvasWrapper(CanvasWrapper const & other) [constructor]

    # CanvasWrapper & CanvasWrapper::operator=(CanvasWrapper rhs) [member operator]

    # CanvasWrapper::~CanvasWrapper() [destructor]
    def __del__(self) -> None: ...

    # void CanvasWrapper::SetPosition(Vector2F pos) [member function]
    def SetPosition(self, pos: Vector2F) -> None: ...

    # Vector2F CanvasWrapper::GetPositionFloat() [member function]
    def GetPositionFloat(self) -> Vector2F: ...

    # void CanvasWrapper::SetColor(char Red, char Green, char Blue, char Alpha) [member function]
    def SetColor(self, Red: int, Green: int, Blue: int, Alpha: int) -> None: ...

    # void CanvasWrapper::SetColor(LinearColor color) [member function]
    def SetColor(self, color: LinearColor) -> None: ...

    # LinearColor CanvasWrapper::GetColor() [member function]
    def GetColor(self) -> LinearColor: ...

    # void CanvasWrapper::DrawBox(Vector2F size) [member function]
    def DrawBox(self, size: Vector2F) -> None: ...

    # void CanvasWrapper::FillBox(Vector2F size) [member function]
    def FillBox(self, size: Vector2F) -> None: ...

    # void CanvasWrapper::FillTriangle(Vector2F p1, Vector2F p2, Vector2F p3) [member function]
    def FillTriangle(self, p1: Vector2F, p2: Vector2F, p3: Vector2F) -> None: ...

    # void CanvasWrapper::FillTriangle(Vector2F p1, Vector2F p2, Vector2F p3, LinearColor color) [member function]
    def FillTriangle(self, p1: Vector2F, p2: Vector2F, p3: Vector2F, color: LinearColor) -> None: ...

    # void CanvasWrapper::DrawString(std::string text) [member function]
    def DrawString(self, text: str) -> None: ...

    # void CanvasWrapper::DrawString(std::string text, float xScale, float yScale) [member function]
    def DrawString(self, text: str, xScale: float, yScale: float) -> None: ...

    # void CanvasWrapper::DrawString(std::string text, float xScale, float yScale, bool dropShadow, bool wrapText=false) [member function]
    def DrawString(self, text: str, xScale: float, yScale: float, dropShadow: bool, wrapText: bool = False) -> None: ...

    # Vector2F CanvasWrapper::GetStringSize(std::string text, float xScale=1, float yScale=1) [member function]
    def GetStringSize(self, text: str, xScale: float = 1, yScale: float = 1) -> Vector2F: ...

    # void CanvasWrapper::DrawLine(Vector2F start, Vector2F end) [member function]
    def DrawLine(self, start: Vector2F, end: Vector2F) -> None: ...

    # void CanvasWrapper::DrawLine(Vector2F start, Vector2F end, float width) [member function]
    def DrawLine(self, start: Vector2F, end: Vector2F, width: float) -> None: ...

    # void CanvasWrapper::DrawRect(Vector2F start, Vector2F end) [member function]
    def DrawRect(self, start: Vector2F, end: Vector2F) -> None: ...

    # void CanvasWrapper::DrawTexture(ImageWrapper * img, float scale) [member function]
    def DrawTexture(self, img: ImageWrapper, scale: float) -> None: ...

    # void CanvasWrapper::DrawRect(float RectX, float RectY, ImageWrapper * img) [member function]
    def DrawRect(self, RectX: float, RectY: float, img: ImageWrapper) -> None: ...

    # void CanvasWrapper::DrawTile(ImageWrapper * img, float XL, float YL, float U, float V, float UL, float VL, LinearColor Color, unsigned int ClipTile, unsigned char Blend) [member function]
    def DrawTile(self, img: ImageWrapper, XL: float, YL: float, U: float, V: float, UL: float, VL: float, Color: LinearColor, ClipTile: int, Blend: int) -> None: ...

    # void CanvasWrapper::DrawRotatedTile(ImageWrapper * img, Rotator & Rotation, float XL, float YL, float U, float V, float UL, float VL, float AnchorX, float AnchorY) [member function]
    def DrawRotatedTile(self, img: ImageWrapper, Rotation: Rotator, XL: float, YL: float, U: float, V: float, UL: float, VL: float, AnchorX: float, AnchorY: float) -> None: ...

    # void CanvasWrapper::SetPosition(Vector2 pos) [member function]
    def SetPosition(self, pos: Vector2) -> None: ...

    # Vector2 CanvasWrapper::GetPosition() [member function]
    def GetPosition(self) -> Vector2: ...

    # void CanvasWrapper::DrawBox(Vector2 size) [member function]
    def DrawBox(self, size: Vector2) -> None: ...

    # void CanvasWrapper::FillBox(Vector2 size) [member function]
    def FillBox(self, size: Vector2) -> None: ...

    # void CanvasWrapper::FillTriangle(Vector2 p1, Vector2 p2, Vector2 p3) [member function]
    def FillTriangle(self, p1: Vector2, p2: Vector2, p3: Vector2) -> None: ...

    # void CanvasWrapper::FillTriangle(Vector2 p1, Vector2 p2, Vector2 p3, LinearColor color) [member function]
    def FillTriangle(self, p1: Vector2, p2: Vector2, p3: Vector2, color: LinearColor) -> None: ...

    # void CanvasWrapper::DrawLine(Vector2 start, Vector2 end) [member function]
    def DrawLine(self, start: Vector2, end: Vector2) -> None: ...

    # void CanvasWrapper::DrawLine(Vector2 start, Vector2 end, float width) [member function]
    def DrawLine(self, start: Vector2, end: Vector2, width: float) -> None: ...

    # void CanvasWrapper::DrawRect(Vector2 start, Vector2 end) [member function]
    def DrawRect(self, start: Vector2, end: Vector2) -> None: ...

    # Vector2 CanvasWrapper::Project(Vector location) [member function]
    def Project(self, location: Vector) -> Vector2: ...

    # Vector2F CanvasWrapper::ProjectF(Vector location) [member function]
    def ProjectF(self, location: Vector) -> Vector2F: ...

    # Vector2 CanvasWrapper::GetSize() [member function]
    def GetSize(self) -> Vector2: ...

    # Private:
    # CanvasWrapper::Impl [class declaration]

    # CanvasWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


