# Copyright (c) 2020-2022 The PyUnity Team
# This file is licensed under the MIT License.
# See https://docs.pyunity.x10.bz/en/latest/license.html

__all__ = ["Material", "Color", "RGB", "HSV"]

import colorsys

class Material:
    """
    Class to hold data on a material.

    Attributes
    ----------
    color : Color
        An albedo tint.
    texture : Texture2D
        A texture to map onto the mesh provided by a MeshRenderer

    """

    def __init__(self, color, texture=None):
        self.color = color
        self.texture = texture

class Color:
    def toString(self):
        return str(self)

    @staticmethod
    def fromString(string):
        if string.startswith("RGB"):
            return RGB(*list(map(int, string[4:-1].split(", "))))
        elif string.startswith("HSV"):
            return HSV(*list(map(int, string[4:-1].split(", "))))

class RGB(Color):
    """
    A class to represent an RGB color.

    Parameters
    ----------
    r : int
        Red value (0-255)
    g : int
        Green value (0-255)
    b : int
        Blue value (0-255)

    """

    def __truediv__(self, other):
        a, b, c = tuple(self)
        return a / other, b / other, c / other

    def __mul__(self, other):
        a, b, c = tuple(self)
        return a * other, b * other, c * other

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __list__(self):
        return [self.r, self.g, self.b]

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b

    def __repr__(self):
        return f"RGB({', '.join(map(str, tuple(self)))})"
    def __str__(self):
        return f"RGB({', '.join(map(str, tuple(self)))})"

    def toRGB(self):
        return self

    def toHSV(self):
        return HSV.fromRGB(self.r, self.g, self.b)

    @staticmethod
    def fromHSV(h, s, v):
        r, g, b = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)
        return RGB(int(r * 255), int(g * 255), int(b * 255))

class HSV(Color):
    """
    A class to represent a HSV color.

    Parameters
    ----------
    h : int
        Hue (0-360)
    s : int
        Saturation (0-100)
    v : int
        Value (0-100)

    """
    def __init__(self, h, s, v):
        self.h = h
        self.s = s
        self.v = v

    def __list__(self):
        return [self.h, self.s, self.v]

    def __iter__(self):
        yield self.h
        yield self.s
        yield self.v

    def __repr__(self):
        return f"HSV({', '.join(map(str, tuple(self)))})"
    def __str__(self):
        return f"HSV({', '.join(map(str, tuple(self)))})"

    def toRGB(self):
        return RGB.fromHSV(self.h, self.s, self.v)

    def toHSV(self):
        return self

    @staticmethod
    def fromRGB(r, g, b):
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        return HSV(int(h * 360), int(s * 100), int(v * 100))
