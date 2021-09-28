__all__ = ["Canvas", "RectData", "RectAnchors",
           "RectOffset", "RectTransform", "Image2D", "Gui",
           "Text", "FontLoader", "GuiComponent",
           "NoResponseGuiComponent", "CheckBox"]

from .errors import PyUnityException
from .values import Vector2, Color, RGB
from .core import Component, SingleComponent, GameObject, ShowInInspector
from .files import Texture2D
from .input import Input, MouseCode, KeyState
from .abc import ABCMeta, abstractmethod
from PIL import Image, ImageDraw, ImageFont
from types import FunctionType
import os
import sys
import enum

class Canvas(Component):
    def Update(self, updated):
        for descendant in self.transform.GetDescendants():
            if descendant in updated:
                continue
            updated.append(descendant)
            comp = descendant.GetComponent(GuiComponent)
            if comp is not None:
                comp.pressed = Input.GetMouse(MouseCode.Left)
                rectTransform = descendant.GetComponent(RectTransform)
                rect = rectTransform.GetRect() + rectTransform.offset
                pos = Vector2(Input.mousePosition)
                if rect.min < pos < rect.max:
                    if Input.GetMouseState(MouseCode.Left, KeyState.UP):
                        comp.Update()

class RectData:
    def __init__(self, min_or_both=None, max=None):
        if min_or_both is None:
            self.min = Vector2.zero()
            self.max = Vector2.zero()
        elif max is None:
            if isinstance(min_or_both, RectData):
                self.min = min_or_both.min.copy()
                self.max = min_or_both.max.copy()
            else:
                self.min = min_or_both.copy()
                self.min = min_or_both.copy()
        else:
            self.min = min_or_both.copy()
            self.max = max.copy()

    def __repr__(self):
        return "<{} min={} max={}>".format(self.__class__.__name__, self.min, self.max)

    def __add__(self, other):
        if isinstance(other, RectData):
            return RectData(self.min + other.min, self.max + other.max)
        else:
            return RectData(self.min + other, self.max + other)

    def __sub__(self, other):
        if isinstance(other, RectData):
            return RectData(self.min - other.min, self.max - other.max)
        else:
            return RectData(self.min - other, self.max - other)

    def __mul__(self, other):
        if isinstance(other, RectData):
            return RectData(self.min * other.min, self.max * other.max)
        else:
            return RectData(self.min * other, self.max * other)

class RectAnchors(RectData):
    def SetPoint(self, p):
        self.min = p.copy()
        self.max = p.copy()

    def RelativeTo(self, other):
        parentSize = other.max - other.min
        absAnchorMin = other.min + (self.min * parentSize)
        absAnchorMax = other.min + (self.max * parentSize)
        return RectData(absAnchorMin, absAnchorMax)

class RectOffset(RectData):
    @staticmethod
    def Square(size, center=Vector2.zero()):
        return RectOffset(center - size / 2, center + size / 2)

    def Move(self, pos):
        self.min += pos
        self.max += pos

    def SetCenter(self, pos):
        size = self.max - self.min
        self.min = pos - size / 2
        self.max = pos + size / 2

class RectTransform(SingleComponent):
    anchors = ShowInInspector(RectAnchors)
    offset = ShowInInspector(RectOffset)
    pivot = ShowInInspector(Vector2)
    rotation = ShowInInspector(float, 0)
    def __init__(self, transform):
        super(RectTransform, self).__init__(transform)
        self.anchors = RectAnchors()
        self.offset = RectOffset()
        self.pivot = Vector2(0.5, 0.5)

        if self.transform.parent is None:
            self.parent = None
        else:
            self.parent = self.transform.parent.GetComponent(RectTransform)

    def GetRect(self):
        from .render import Screen
        if self.parent is None:
            return self.anchors * Screen.size
        else:
            parentRect = self.parent.GetRect() + self.parent.offset
            rect = self.anchors.RelativeTo(parentRect)
            return rect

class GuiComponent(Component, metaclass=ABCMeta):
    @abstractmethod
    def Update(self):
        pass

class NoResponseGuiComponent(GuiComponent):
    def Update(self):
        pass

class Image2D(NoResponseGuiComponent):
    texture = ShowInInspector(Texture2D)
    def __init__(self, transform):
        super(Image2D, self).__init__(transform)
        self.rectTransform = self.GetComponent(RectTransform)

class Button(GuiComponent):
    callback = ShowInInspector(FunctionType, lambda: None)
    state = ShowInInspector(KeyState, KeyState.UP)
    mouseButton = ShowInInspector(MouseCode, MouseCode.Left)
    pressed = ShowInInspector(bool, False)

    def Update(self):
        self.callback()

textureDir = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "shaders", "gui", "textures")
buttonDefault = Texture2D(os.path.join(textureDir, "button.png"))
checkboxDefaults = [
    Texture2D(os.path.join(textureDir, "checkboxOff.png")),
    Texture2D(os.path.join(textureDir, "checkboxOn.png"))
]

class _FontLoader:
    fonts = {}

    @classmethod
    def LoadFont(cls, name, size):
        if os.getenv("PYUNITY_TESTING") is not None:
            return None
        if name in cls.fonts:
            if size in cls.fonts[name]:
                return cls.fonts[name][size]
        else:
            cls.fonts[name] = {}
        file = cls.LoadFile(name)
        font = ImageFont.truetype(file, size)
        fontobj = Font(name, size, font)
        cls.fonts[name][size] = fontobj
        return fontobj

    @classmethod
    def LoadFile(cls, name):
        raise PyUnityException("No font loading function found")

class WinFontLoader(_FontLoader):
    @classmethod
    def LoadFile(cls, name):
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts\\")
        try:
            file = winreg.QueryValueEx(key, name + " (TrueType)")
        except WindowsError:
            file = None
        if file is None:
            raise PyUnityException(f"Cannot find font called {name!r}")
        return file[0]

class UnixFontLoader(_FontLoader):
    @classmethod
    def LoadFile(cls, name):
        import subprocess
        process = subprocess.Popen(["fc-match", name], stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        out = stdout.decode()
        if out == "":
            raise PyUnityException(f"Cannot find font called {name!r}")

        return out.split(": ")[0]

if sys.platform.startswith("linux") or sys.platform == "darwin":
    FontLoader = UnixFontLoader
else:
    FontLoader = WinFontLoader

class Font:
    def __init__(self, name, size, imagefont):
        if not isinstance(imagefont, ImageFont.FreeTypeFont):
            raise PyUnityException("Please specify a FreeType font" +
                                   "created from ImageFont.freetype")

        self._font = imagefont
        self.name = name
        self.size = size

    def __reduce__(self):
        return (FontLoader.LoadFont, (self.name, self.size))

class TextAlign(enum.IntEnum):
    Left = enum.auto()
    Center = enum.auto()
    Right = enum.auto()

class Text(NoResponseGuiComponent):
    font = ShowInInspector(Font, FontLoader.LoadFont("Arial", 24))
    text = ShowInInspector(str, "Text")
    color = ShowInInspector(Color)
    depth = ShowInInspector(float, 0.1)
    centeredX = ShowInInspector(TextAlign, TextAlign.Left)
    centeredY = ShowInInspector(TextAlign, TextAlign.Center)
    def __init__(self, transform):
        super(Text, self).__init__(transform)
        self.rect = None
        self.texture = None
        self.color = RGB(255, 255, 255)

    def GenTexture(self):
        if self.rect is None:
            self.rect = self.GetComponent(RectTransform)
            if self.rect is None:
                return

        rect = self.rect.GetRect() + self.rect.offset
        size = (rect.max - rect.min).abs()
        im = Image.new("RGBA", tuple(size), (255, 255, 255, 0))

        draw = ImageDraw.Draw(im)
        width, height = draw.textsize(self.text, font=self.font._font)
        if self.centeredX == TextAlign.Left:
            offX = 0
        elif self.centeredX == TextAlign.Center:
            offX = (size.x - width) // 2
        else:
            offX = size.x - width
        if self.centeredY == TextAlign.Left:
            offY = 0
        elif self.centeredY == TextAlign.Center:
            offY = (size.y - height) // 2
        else:
            offY = size.y - height

        draw.text((offX, offY), self.text, font=self.font._font,
                  fill=tuple(self.color))
        if self.texture is not None:
            self.texture.setImg(im)
        else:
            self.texture = Texture2D(im)

    def __setattr__(self, name, value):
        super(Text, self).__setattr__(name, value)
        if name in ["font", "text", "color"]:
            if self.gameObject.scene is not None:
                self.GenTexture()

class CheckBox(GuiComponent):
    checked = ShowInInspector(bool, False)
    def __init__(self, transform):
        super(CheckBox, self).__init__(transform)

    def Update(self):
        self.checked = not self.checked
        self.GetComponent(Image2D).texture = checkboxDefaults[int(self.checked)]

class Gui:
    @classmethod
    def MakeButton(cls, name, scene, text="Button", font=None, color=None, texture=None):
        if texture is None:
            texture = buttonDefault

        button = GameObject(name)
        transform = button.AddComponent(RectTransform)
        buttonComponent = button.AddComponent(Button)

        textureObj = GameObject("Button", button)
        transform2 = textureObj.AddComponent(RectTransform)
        transform2.anchors = RectAnchors(Vector2.zero(), Vector2.one())
        img = textureObj.AddComponent(Image2D)
        img.texture = texture

        textObj = GameObject("Text", button)
        transform3 = textObj.AddComponent(RectTransform)
        transform3.anchors = RectAnchors(Vector2.zero(), Vector2.one())

        textComp = textObj.AddComponent(Text)
        textComp.text = text
        if font is None:
            font = FontLoader.LoadFont("Arial", 16)
        textComp.font = font
        if color is None:
            color = RGB(0, 0, 0)
        textComp.color = color
        textComp.centeredX = TextAlign.Center

        scene.Add(button)
        scene.Add(textureObj)
        return transform, buttonComponent, textComp
    
    @classmethod
    def MakeCheckBox(cls, name, scene):
        box = GameObject(name)
        transform = box.AddComponent(RectTransform)
        checkbox = box.AddComponent(CheckBox)
        img = box.AddComponent(Image2D)
        img.texture = checkboxDefaults[0]
        scene.Add(box)
        return transform, checkbox
