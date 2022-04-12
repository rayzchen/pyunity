# Copyright (c) 2020-2022 The PyUnity Team
# This file is licensed under the MIT License.
# See https://docs.pyunity.x10.bz/en/latest/license.html

from typing import Optional, Any

class Clock:
    _fps: int = ...
    _frameDuration: float = ...

    def __init__(self) -> None: ...
    def Start(self, fps: Optional[int] = ...) -> None: ...
    def Maintain(self) -> float: ...

    @property
    def fps(self) -> float: ...
    @fps.setter
    def fps(self, value: float) -> None: ...

class ImmutableStruct(type):
    _names: str
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def _set(self, name: str, value: Any) -> None: ...
