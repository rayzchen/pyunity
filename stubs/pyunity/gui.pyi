## Copyright (c) 2020-2023 The PyUnity Team
## This file is licensed under the MIT License.
## See https://docs.pyunity.x10.bz/en/latest/license.html

__all__ = ["Button", "Canvas", "CheckBox", "Font", "FontLoader", "Gui",
           "GuiComponent", "GuiRenderComponent", "Image2D",
           "NoResponseGuiComponent", "RectAnchors", "RectData", "RectOffset",
           "RectTransform", "RenderTarget", "Text", "TextAlign",
           "UnixFontLoader", "WinFontLoader"]

from .core import Component, SingleComponent
from .events import EventLoop
from .files import Texture2D
from .input import KeyState, MouseCode
from .meshes import Color
from .render import Camera
from .scenes import Scene
from .values import ABCMeta, Vector2, abstractmethod
from PIL import ImageFont
from typing import Any, Dict, List, Tuple, Union, Callable, Optional
from pathlib import Path
import enum

_RAQM_SUPPORT: bool = ...

class Canvas(Component):
    def Update(self, loop: EventLoop) -> None: ...

class RectData:
    min: Vector2
    max: Vector2
    def __init__(self, minOrBoth: Optional[Union[Vector2, RectData]] = ..., max: Optional[Vector2] = ...) -> None: ...
    def size(self) -> Vector2: ...
    def SetPoint(self, pos: Vector2) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Union[RectData, Any]) -> bool: ...
    def __hash__(self) -> int: ...
    def __add__(self, other: Union[RectData, Vector2, float]) -> RectData: ...
    def __sub__(self, other: Union[RectData, Vector2, float]) -> RectData: ...
    def __mul__(self, other: Union[RectData, Vector2, float]) -> RectData: ...

class RectAnchors(RectData):
    def RelativeTo(self, other: RectData) -> RectData: ...

class RectOffset(RectData):
    @staticmethod
    def Rectangle(size: Vector2, center: Vector2 = ...) -> RectOffset: ...
    def Move(self, pos: Vector2) -> None: ...
    def SetCenter(self, pos: Vector2) -> None: ...

class RectTransform(SingleComponent):
    anchors: Union[RectAnchors, None] = ...
    offset: Union[RectOffset, None] = ...
    pivot: Union[Vector2, None] = ...
    rotation: float = ...
    @property
    def parent(self) -> RectTransform: ...
    def __init__(self) -> None: ...
    def GetRect(self, bb: Optional[Vector2] = ...) -> RectData: ...

class GuiComponent(Component, metaclass=ABCMeta):
    @abstractmethod
    async def HoverUpdate(self) -> None: ...

class NoResponseGuiComponent(GuiComponent): ...

class GuiRenderComponent(NoResponseGuiComponent):
    flipX: int = ...
    flipY: int = ...

    def PreRender(self) -> None: ...

class Image2D(GuiRenderComponent):
    texture: Union[Texture2D, None] = ...
    depth: float = ...
    rectTransform: RectTransform
    def __init__(self) -> None: ...

class RenderTarget(GuiRenderComponent):
    source: Union[Camera, None] = ...
    depth: float = ...
    canvas: bool = ...
    setup: bool
    size: Vector2
    texture: int
    renderPass: bool
    def __init__(self) -> None: ...
    def PreRender(self) -> None: ...
    def saveImg(self, path: Union[str, Path]) -> None: ...
    def genBuffers(self, force: bool = ...) -> None: ...
    def setSize(self, size: Vector2) -> None: ...

class Button(GuiComponent):
    callback: Union[Callable[[], None], None] = ...
    state: KeyState = ...
    mouseButton: MouseCode = ...
    pressed: bool = ...

buttonDefault: Texture2D = ...
checkboxDefaults: List[Texture2D] = ...

class _FontLoader:
    fonts: Dict[str, Font]

    @classmethod
    def ChooseFont(cls, names: List[str], size: int) -> Font: ...
    @classmethod
    def LoadFont(cls, name: str, size: int) -> Font: ...
    @classmethod
    def FromFile(cls, name: str, file: str, size: int) -> Union[Font, None]: ...
    @classmethod
    def LoadFile(cls, name: str) -> str: ...

class WinFontLoader(_FontLoader):
    localFontRegPath: Union[str, None]
    @classmethod
    def getLocalFontRegPath(cls) -> str: ...
    @classmethod
    def LoadFile(cls, name: str) -> str: ...

class UnixFontLoader(_FontLoader):
    @classmethod
    def LoadFile(cls, name: str) -> str: ...

class FontLoader(_FontLoader): ...

class Font:
    _font: ImageFont.FreeTypeFont
    name: str
    size: int
    def __init__(self, name: str, size: int, imagefont: ImageFont.FreeTypeFont) -> None: ...
    def __reduce__(self) -> Tuple[Callable[[str, int], Font], Tuple[str, int]]: ...

class TextAlign(enum.IntEnum):
    Left: TextAlign = ...
    Center: TextAlign = ...
    Right: TextAlign = ...
    Top: TextAlign = ...
    Bottom: TextAlign = ...

class Text(GuiRenderComponent):
    font: Font = ...
    text: str = ...
    color: Union[Color, None] = ...
    depth: float = ...
    centeredX: TextAlign = ...
    centeredY: TextAlign = ...
    rect: RectTransform
    texture: Texture2D
    def __init__(self) -> None: ...
    def PreRender(self) -> None: ...
    def GenTexture(self) -> None: ...
    def __setattr__(self, name: str, value: object) -> None: ...

class CheckBox(GuiComponent):
    checked: bool = ...

class Gui:
    @classmethod
    def MakeButton(
        cls, name: str, scene: Scene, text: str = ...,
        font: Optional[Font] = ..., color: Optional[Color] = ...,
        texture: Optional[Texture2D] = ...) -> Tuple[RectTransform, Button, Text]: ...
    @classmethod
    def MakeCheckBox(cls, name: str, scene: Scene) -> Tuple[RectTransform, CheckBox]: ...
