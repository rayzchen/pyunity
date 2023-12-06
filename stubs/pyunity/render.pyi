## Copyright (c) 2020-2023 The PyUnity Team
## This file is licensed under the MIT License.
## See https://docs.pyunity.x10.bz/en/latest/license.html

"""
Classes to aid in rendering in a Scene.

"""

__all__ = ["Camera", "Screen", "Shader", "Light", "LightType"]

from .core import SingleComponent, Transform
from .files import Skybox
from .gui import Canvas, GuiRenderComponent, RectTransform
from .meshes import Color, MeshRenderer
from .values import ImmutableStruct, Quaternion, Vector2, Vector3
import glm
from typing import Dict, List, Union, Optional
from pathlib import Path
import enum

def fillScreen(scale: float = ...) -> None: ...

class Shader:
    VERSION: str = ...
    vertex: str
    frag: str
    compiled: bool
    name: str
    uniforms: Dict[str, Union[int, float, glm.vec3, glm.mat3, glm.mat4]]
    def __init__(self, vertex: str, frag: str, name: str) -> None: ...
    def __deepcopy__(self, memo: Optional[Dict[int, object]] = ...) -> Shader: ...
    def loadCache(self, file: Union[str, Path]) -> None: ...
    def compile(self) -> None: ...
    @staticmethod
    def fromFolder(path: Union[str, Path], name: str) -> Shader: ...
    def setVec3(self, var: bytes, val: glm.vec3) -> None: ...
    def setMat3(self, var: bytes, val: glm.mat3) -> None: ...
    def setMat4(self, var: bytes, val: glm.mat4) -> None: ...
    def setInt(self, var: bytes, val: int) -> None: ...
    def setFloat(self, var: bytes, val: float) -> None: ...
    def use(self) -> None: ...

shaders: Dict[str, Shader] = ...
skyboxes: Dict[str, Skybox] = ...

def compileShaders() -> None: ...
def compileSkyboxes() -> None: ...
def resetShaders() -> None: ...
def resetSkyboxes() -> None: ...

class LightType(enum.IntEnum):
    Point: LightType = ...
    Directional: LightType = ...
    Spot: LightType = ...

class Light(SingleComponent):
    intensity: int = ...
    color: Color = ...
    type: LightType = ...
    near: float
    far: float
    def __init__(self) -> None: ...
    def setupBuffers(self, depthMapSize: int) -> None: ...

class Camera(SingleComponent):
    near: float = ...
    far: float = ...
    clearColor: Union[Color, None] = ...
    shader: Shader = ...
    skyboxEnabled: bool = ...
    skybox: Skybox = ...
    ortho: bool = ...
    shadows: bool = ...
    canvas: Union[Canvas, None] = ...
    depthMapSize: int = ...
    size: Vector2
    guiShader: Shader
    skyboxShader: Shader
    depthShader: Shader
    customProjMat: Union[glm.mat4, None]
    orthoMat: glm.mat4
    viewMat: glm.mat4
    renderPass: bool
    guiVBO: int
    guiVAO: int
    _fov: float
    _orthoSize: float

    def __init__(self) -> None: ...
    def setupBuffers(self) -> None: ...
    @property
    def fov(self) -> float: ...
    @fov.setter
    def fov(self, value: float) -> None: ...
    @property
    def orthoSize(self) -> float: ...
    @orthoSize.setter
    def orthoSize(self, value: float) -> None: ...
    def Resize(self, width: int, height: int) -> None: ...
    def getMatrix(self, transform: Transform) -> glm.mat4: ...
    def get2DMatrix(self, rectTransform: RectTransform) -> glm.mat4: ...
    def getViewMat(self) -> glm.mat4: ...
    def UseShader(self, name: str) -> None: ...
    def SetupShader(self, lights: List[Light]) -> None: ...
    def SetupDepthShader(self, light: Light) -> None: ...
    def Draw(self, renderers: List[MeshRenderer]) -> None: ...
    def DrawDepth(self, renderers: List[MeshRenderer]) -> None: ...
    def RenderDepth(self, renderers: List[MeshRenderer], lights: List[Light]) -> None: ...
    def RenderScene(self, renderers: List[MeshRenderer], lights: List[Light]) -> None: ...
    def Render(self, renderers: List[MeshRenderer], lights: List[Light]) -> None: ...
    def RenderSkybox(self) -> None: ...
    def Render2D(self) -> None: ...
    def Setup2D(self) -> None: ...
    def Draw2D(self, renderers: List[GuiRenderComponent]) -> None: ...

class Screen(metaclass=ImmutableStruct):
    _names: List[str] = ...
    width: int = ...
    height: int = ...
    size: Vector2 = ...
    aspect: float = ...
    @classmethod
    def _edit(cls, width: int, height: int) -> None: ...
