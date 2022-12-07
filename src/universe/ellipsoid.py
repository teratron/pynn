from typing import Optional


class Ellipsoid:
    def __init__(self, radius: Optional[list[float]] = None):
        self._radius: list[float] = radius
