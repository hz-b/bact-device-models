import functools
from dataclasses import dataclass
from typing import Sequence, Hashable, Dict


@dataclass
class BPMPosition:
    """
    """
    x: float
    y: float


@dataclass
class BPMButtons:
    """
    todo:
        consider renaming bpm buttons to give them mre meaning
    """
    a: float
    b: float
    c: float
    d: float


@dataclass
class BPMReading:
    name: Hashable
    pos: BPMPosition
    btns: BPMButtons


@dataclass
class Orbit:
    orbit: Sequence[BPMReading]

    def identifiers(self) -> Sequence[Hashable]:
        return tuple(self._lut.keys())

    def get_element(self, id_: Hashable) -> BPMReading:
        """
        Todo:
            consider to return a more descriptive Exception if
            identifer is not found
        """
        return self._lut[id_]

    @functools.cached_property
    def _lut(self) -> Dict[Hashable, BPMReading]:
        return {elem.name: elem for elem in self.orbit}

