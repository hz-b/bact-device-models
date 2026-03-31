from dataclasses import dataclass
from functools import cached_property
from typing import Sequence, Dict

from bact_device_models.devices.data_window import DataWindow


@dataclass
class BPMTurnByTurnData:
    """each value for one turn, typically in nm"""
    x: Sequence[int]
    y: Sequence[int]
    sum: Sequence[int]

    timestamp: float
    name: str

    #: which data was selected
    sliced : DataWindow


@dataclass
class BPMTurnByTurnDataCollection:
    col: Sequence[BPMTurnByTurnData]

    def get(self, id_: str) -> BPMTurnByTurnData:
        return self._dict[id_]

    @cached_property
    def _dict(self) -> Dict[str, BPMTurnByTurnData]:
        return {data.name: data for data in self.col}
