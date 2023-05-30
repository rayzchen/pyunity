## Copyright (c) 2020-2022 The PyUnity Team
## This file is licensed under the MIT License.
## See https://docs.pyunity.x10.bz/en/latest/license.html

"""
Utility functions to log output of PyUnity.

This will be imported as ``pyunity.Logger``.

"""

from typing import Callable, Tuple, IO, Union, Any, Type
from types import TracebackType
import atexit

def get_tmp() -> str: ...

folder: str = ...
stream: IO[str] = ...
timestamp: str = ...
start: float = ...

class Level:
    abbr: str
    name: str
    def __init__(self, abbr: str, name: str) -> None: ...
    def __eq__(self, other: Union[Level, Any]) -> bool: ...
    def __hash__(self) -> int: ...

OUTPUT: Level = ...
INFO: Level = ...
DEBUG: Level = ...
ERROR: Level = ...
WARN: Level = ...

class Special:
    func: Callable[[None], str]
    def __init__(self, func: Callable[[None], str]) -> None: ...

class Elapsed:
    def __init__(self) -> None: ...
    def tick(self) -> float: ...

elapsed: Elapsed = ...
RUNNING_TIME: Special = ...
ELAPSED_TIME: Special = ...

def Log(*mesage: str, stacklevel: int = ...) -> None: ...
def LogLine(level: Level, *message: str, stacklevel: int = ..., silent: bool=...) -> Tuple[float, str]: ...
def LogException(e: Exception, stacklevel: int = ...) -> None: ...
def LogTraceback(exctype: Type[BaseException], value: Union[BaseException, None], tb: Union[TracebackType, None], stacklevel: int = ...) -> None: ...
def LogSpecial(level: Level, type: Special, stacklevel: int = ...) -> None: ...
@atexit.register
def Save() -> None: ...

class TempRedirect:
    def __init__(self, *, silent: bool = ...) -> None: ...
    def get(self) -> str: ...
    def __enter__(self) -> TempRedirect: ...
    def __exit__(self, exctype: Type[BaseException], value: Union[BaseException, None], tb: Union[TracebackType, None]) -> None: ...

def SetStream(s: IO[str]) -> None: ...
def ResetStream() -> None: ...
