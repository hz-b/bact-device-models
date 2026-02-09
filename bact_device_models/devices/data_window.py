from dataclasses import dataclass
from typing import Optional


@dataclass
class DataWindow:
    start: Optional[int] = None
    stop: Optional[int] = None
    step: Optional[int] = None

    def __post_init__(self) -> None:
        self.start = validate_slice_index("start", self.start)
        self.stop = validate_slice_index("stop", self.stop)
        self.step = validate_slice_index("step", self.step)

        if self.step == 0:
            raise ValueError("step cannot be 0")

    @classmethod
    def from_slice(cls, s: slice):
        return cls(start=s.start, stop=s.stop, step=s.step)

    def as_slice(self) -> slice:
        return slice(self.start, self.stop, self.step)


def validate_slice_index(name: str, value: Optional[int]) -> Optional[int]:
    if value is None:
        return None
    if not isinstance(value, int):
        raise TypeError(f"{name} must be int or None, got {type(value).__name__}")
    return value


__all__ = ["DataWindow"]
