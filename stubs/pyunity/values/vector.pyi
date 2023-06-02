## Copyright (c) 2020-2023 The PyUnity Team
## This file is licensed under the MIT License.
## See https://docs.pyunity.x10.bz/en/latest/license.html

__all__ = ["Vector", "Vector2", "Vector3"]

from typing import Callable, Iterator, TypeVar, List, Union, Optional, Tuple
from .abc import ABCMeta, abstractmethod, abstractproperty
from .other import LockedLiteral

def conv(num: Union[int, float]) -> str: ...

T = TypeVar("T", bound=Vector)

class Vector(LockedLiteral, metaclass=ABCMeta):
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __getitem__(self) -> float: ...
    @abstractmethod
    def __iter__(self) -> Iterator[float]: ...
    def __list__(self) -> List[float]: ...
    def __hash__(self) -> int: ...
    @abstractmethod
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def _o1(self, f: Callable[[float], float]) -> Vector: ...
    def _o2(self, other: Union[T, float], f: Callable[[float, float], float]) -> T: ...
    def _o2r(self, other: Union[T, float], f: Callable[[float, float], float]) -> T: ...
    def __add__(self, other: Union[T, float]) -> T: ...
    def __radd__(self, other: Union[T, float]) -> T: ...
    def __sub__(self, other: Union[T, float]) -> T: ...
    def __rsub__(self, other: Union[T, float]) -> T: ...
    def __mul__(self, other: Union[T, float]) -> T: ...
    def __rmul__(self, other: Union[T, float]) -> T: ...
    def __div__(self, other: Union[T, float]) -> T: ...
    def __rdiv__(self, other: Union[T, float]) -> T: ...
    def __floordiv__(self, other: Union[T, float]) -> T: ...
    def __rfloordiv__(self, other: Union[T, float]) -> T: ...
    def __truediv__(self, other: Union[T, float]) -> T: ...
    def __rtruediv__(self, other: Union[T, float]) -> T: ...
    def __mod__(self, other: Union[T, float]) -> T: ...
    def __rmod__(self, other: Union[T, float]) -> T: ...
    def __lshift__(self, other: Union[T, float]) -> T: ...
    def __rlshift__(self, other: Union[T, float]) -> T: ...
    def __rshift__(self, other: Union[T, float]) -> T: ...
    def __rrshift__(self, other: Union[T, float]) -> T: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: Union[T, float]) -> bool: ...
    def __ge__(self, other: Union[T, float]) -> bool: ...
    def __lt__(self, other: Union[T, float]) -> bool: ...
    def __le__(self, other: Union[T, float]) -> bool: ...
    def __and__(self, other: Union[T, float]) -> T: ...
    def __rand__(self, other: Union[T, float]) -> T: ...
    def __or__(self, other: Union[T, float]) -> T: ...
    def __ror__(self, other: Union[T, float]) -> T: ...
    def __xor__(self, other: Union[T, float]) -> T: ...
    def __rxor__(self, other: Union[T, float]) -> T: ...
    def __neg__(self) -> T: ...
    def __pos__(self) -> T: ...
    def __abs__(self) -> T: ...
    def abs(self) -> float: ...
    def __round__(self, other: Optional[int] = ...) -> T: ...
    def __invert__(self) -> T: ...
    @abstractproperty
    def length(self) -> float: ...
    @property
    def intTuple(self) -> Tuple[int, ...]: ...
    @abstractmethod
    def replace(self, num: int, value: float) -> None: ...

class Vector2(Vector):
    x: float
    y: float
    def __init__(self, x_or_list: Optional[float] = ..., y: Optional[float] = ...) -> None: ...
    def _o1(self, f: Callable[[float], float]) -> Vector2: ...
    def _o2(self, other: Union[T, float], f: Callable[[float, float], float]) -> T: ...
    def _o2r(self, other: Union[T, float], f: Callable[[float, float], float]) -> T: ...
    def copy(self) -> Vector2: ...
    def getLengthSqrd(self) -> float: ...
    def normalized(self) -> Vector2: ...
    def normalizeReturnLength(self) -> float: ...
    def getDistance(self) -> float: ...
    def getDistSqrd(self) -> float: ...
    def clamp(self, min: Vector2, max: Vector2) -> None: ...
    def dot(self, other: Vector2) -> Vector2: ...
    def cross(self, other: Vector2) -> Vector2: ...

    @staticmethod
    def zero() -> Vector2: ...
    @staticmethod
    def one() -> Vector2: ...
    @staticmethod
    def up() -> Vector2: ...
    @staticmethod
    def down() -> Vector2: ...
    @staticmethod
    def left() -> Vector2: ...
    @staticmethod
    def right() -> Vector2: ...
    @staticmethod
    def min(a: Vector2, b: Vector2) -> Vector2: ...
    @staticmethod
    def max(a: Vector2, b: Vector2) -> Vector2: ...

    @property
    def intTuple(self) -> tuple: ...
    @property
    def rounded(self) -> tuple: ...

class Vector3(Vector):
    x: float
    y: float
    z: float
    def __init__(self, x_or_list: float = ..., y: float = ..., z: float = ...) -> None: ...
    def _o1(self, f: Callable[[float], float]) -> Vector3: ...
    def _o2(self, other: Union[T, float], f: Callable[[float, float], float]) -> T: ...
    def _o2r(self, other: Union[T, float], f: Callable[[float, float], float]) -> T: ...
    def copy(self) -> Vector3: ...
    def getLengthSqrd(self) -> float: ...
    def normalized(self) -> Vector3: ...
    def normalizeReturnLength(self) -> float: ...
    def getDistance(self) -> float: ...
    def getDistSqrd(self) -> float: ...
    def clamp(self, min: Vector3, max: Vector3) -> None: ...
    def dot(self, other: Vector3) -> Vector3: ...
    def cross(self, other: Vector3) -> Vector3: ...

    @staticmethod
    def zero() -> Vector3: ...
    @staticmethod
    def one() -> Vector3: ...
    @staticmethod
    def forward() -> Vector3: ...
    @staticmethod
    def back() -> Vector3: ...
    @staticmethod
    def up() -> Vector3: ...
    @staticmethod
    def down() -> Vector3: ...
    @staticmethod
    def left() -> Vector3: ...
    @staticmethod
    def right() -> Vector3: ...
    @staticmethod
    def min(a: Vector3, b: Vector3) -> Vector3: ...
    @staticmethod
    def max(a: Vector3, b: Vector3) -> Vector3: ...

    @property
    def intTuple(self) -> tuple: ...
    @property
    def rounded(self) -> tuple: ...
