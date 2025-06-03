from dataclasses import dataclass
from typing import Sequence


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
    name: str
    pos: BPMPosition
    btns: BPMButtons


@dataclass
class Orbit:
    orbit: Sequence[BPMReading]