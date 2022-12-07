from typing import Optional

from .ellipsoid import Ellipsoid


class Sphere(Ellipsoid):
    def __init__(self, radius: Optional[list[float]] = None):
        super().__init__(radius)
        self.radius: list[float] = radius
