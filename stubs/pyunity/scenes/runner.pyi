## Copyright (c) 2020-2023 The PyUnity Team
## This file is licensed under the MIT License.
## See https://docs.pyunity.x10.bz/en/latest/license.html

__all__ = ["ChangeScene", "Runner", "WindowRunner", "NonInteractiveRunner"]

from ..events import EventLoopManager
from ..window import ABCWindow
from .scene import Scene
from typing import Type, Union, NoReturn

class ChangeScene(Exception): ...

class Runner:
    scene: Union[Scene, None]
    next: Union[Scene, None]
    opened: bool
    eventLoopManager: EventLoopManager
    def __init__(self) -> None: ...
    def setScene(self, scene: Scene) -> None: ...
    def setNext(self, scene: Scene) -> NoReturn: ...
    def open(self) -> None: ...
    def setup(self) -> None: ...
    def load(self, managerClass: Type[EventLoopManager] = ...) -> None: ...
    def start(self) -> None: ...
    def changeScene(self) -> None: ...
    def quit(self) -> None: ...

class WindowRunner(Runner):
    window: ABCWindow
    def open(self) -> None: ...
    def setup(self) -> None: ...
    def load(self, managerClass: Type[EventLoopManager] = ...) -> None: ...
    def start(self) -> None: ...
    def quit(self) -> None: ...

class NonInteractiveRunner(Runner):
    def load(self, managerClass: Type[EventLoopManager] = ...) -> None: ...

def newRunner() -> Runner: ...
