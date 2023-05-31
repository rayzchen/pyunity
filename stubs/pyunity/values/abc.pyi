## Copyright (c) 2020-2023 The PyUnity Team
## This file is licensed under the MIT License.
## See https://docs.pyunity.x10.bz/en/latest/license.html

__all__ = ["ABCMessage", "ABCException", "ABCMeta",
           "abstractmethod", "abstractproperty"]

from typing import Callable, Optional, Type, List, Tuple, Any, NoReturn, Mapping
import inspect

class ABCException(Exception): ...
class ABCMessage(ABCException): ...

class abstractmethod:
    func: Callable[..., Any]
    args: List[Tuple[str, inspect._ParameterKind]]
    def __init__(self, func: Callable[..., Any]) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __get__(self, instance: Any, owner: Optional[Type[abstractmethod]] = ...) -> object: ...
    @staticmethod
    def getargs(func: Callable[..., Any]) -> List[Tuple[str, inspect._ParameterKind]]: ...

class abstractproperty(abstractmethod):
    def __get__(self, instance: Any, owner: Optional[Type[abstractmethod]] = ...) -> object: ...
    def __set__(self, instance: Any, value: object) -> NoReturn: ...
    def __eq__(self, other: object) -> bool: ...

class ABCMeta(type):
    _trigger: bool = ...
    def __init__(cls, fullname: str, bases: Tuple[type, ...], attrs: dict[str, Any], /, **kwds: Any) -> None: ...
    @classmethod
    def __prepare__(cls: Type[Any], fullname: str, bases: Tuple[type, ...], /, **kwds: Any) -> Mapping[str, object]: ...
