"""
Module to load files and scripts.
Also manages project structure.

"""

__all__ = ["Behaviour", "Texture2D", "Prefab",
           "File", "Project", "Skybox", "Scripts"]

from typing import List, Dict, Optional, Type, Union, Tuple
from types import ModuleType
from PIL import Image
from .core import Component, ShowInInspector, GameObject
from .values import Material
import _ctypes

def convert(type: _ctypes.PyCSimpleType, list: List[float]) -> object: ...

class Behaviour(Component):
    _script: ShowInInspector = ...
    def Start(self) -> None: ...
    def Update(self, dt: float) -> None: ...
    def FixedUpdate(self, dt: float) -> None: ...
    def LateUpdate(self, dt: float) -> None: ...

class Scripts:
    var: Dict[int, ModuleType] = ...
    @staticmethod
    def CheckScript(text: str) -> bool: ...
    @staticmethod
    def LoadScripts(path: str) -> ModuleType: ...

class Texture2D:
    path: str
    img: Image.Image
    img_data: bytes
    loaded: bool
    texture: int
    def __init__(self, path_or_im: Union[str, Image.Image]) -> None: ...
    def load(self) -> None: ...
    def setImg(self, im: Image.Image) -> None: ...
    def use(self) -> None: ...

class Skybox:
    names: List[str] = ...
    points: List[int] = ...
    path: str
    compiled: bool
    images: List[Image.Image]
    def __init__(self, path: str) -> None: ...
    def compile(self) -> None: ...
    def use(self) -> None: ...

class Prefab:
    gameObject: GameObject
    components: List[Component]
    def __init__(self, gameObject: GameObject, components: List[Component]) -> None: ...

class File:
    path: str
    type: Union[Type, str]
    uuid: str
    obj: object
    def __init__(self, path: str, type: Union[Type, str], uuid: Optional[str]) -> None: ...

class Project:
    path: str
    name: str
    firstScene: int
    files: Dict[str, Tuple[File, str]]
    file_paths: Dict(str, File)
    def __init__(self, path: str, name: str) -> None: ...
    def import_file(self, localPath: str, type: Union[Type, str], uuid: str) -> File: ...
    def reimport_file(self, localPath: str) -> File: ...
    def get_file_obj(self, uuid: str) -> object: ...
    def write_project(self) -> None: ...
    def save_mat(self, mat: Material, name: str): ...
    def load_mat(self, file: str) -> Material: ...

    @staticmethod
    def from_folder(filePath: str) -> Project: ...
