## Copyright (c) 2020-2023 The PyUnity Team
## This file is licensed under the MIT License.
## See https://docs.pyunity.x10.bz/en/latest/license.html

__all__ = ["LiveDict", "Database"]

from typing import Dict, Iterator, Optional, Generic, TypeVar
from collections.abc import KeysView, ValuesView, ItemsView
from pathlib import Path

KT = TypeVar("KT")
VT = TypeVar("VT")

class LiveDict(Generic[KT, VT]):
    d: Dict[KT, VT]
    parent: Optional[LiveDict]
    def __init__(self, d: Dict, parent: Optional[LiveDict] = ...) -> None: ...
    def __getitem__(self, item: KT) -> VT: ...
    def __setitem__(self, item: KT, value: VT) -> None: ...
    def __delitem__(self, item: KT) -> None: ...
    def __contains__(self, item: VT) -> bool: ...
    def __iter__(self) -> Iterator[VT]: ...
    def update(self) -> None: ...
    def todict(self) -> Dict[KT, VT]: ...
    def keys(self) -> KeysView: ...
    def values(self) -> ValuesView: ...
    def items(self) -> ItemsView: ...
    def pop(self, item: KT) -> VT: ...

class Database(LiveDict[KT, VT]):
    path: str
    def __init__(self, path: str) -> None: ...
    def update(self) -> None: ...
    def refresh(self) -> None: ...

file: Path = ...
db: Database = ...
