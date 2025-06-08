import functools
from dataclasses import dataclass

from typing import Sequence, Union


@dataclass
class BPMElementPosition:
    #: in nanometer
    x: float
    #: in nanometer
    y: float


@dataclass
class BPMElementSignalFromButtons:
    """Beam position monitor readings from the buttons

    Todo:
        find out what the units of these signals are in reality
    """
    a: float
    b: float
    c: float
    d: float


@dataclass
class BPMElement:
    name: str
    pos: BPMElementPosition
    sig: BPMElementSignalFromButtons


@dataclass
class BPMElementList:
    bpms: Sequence[BPMElement]

    def get_element(self, name: str) -> BPMElement:
        return self._lut[name]

    @functools.cached_property
    def _lut(self):
        return {elem.name: elem for elem in self.bpms}
