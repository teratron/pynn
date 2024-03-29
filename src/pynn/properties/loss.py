import math

from typing import Callable, Iterable, Union


class LossMode:
    """The mode of calculation of the total error:

    * MSE -- Mean Squared Error (0);
    * RMSE -- Root Mean Squared Error (1);
    * ARCTAN -- Arctan Error (2);
    * AVG -- Average Error (3).
    """

    MSE: int = 0
    """MSE -- Mean Squared Error (0)."""

    RMSE: int = 1
    """RMSE -- Root Mean Squared Error (1)."""

    ARCTAN: int = 2
    """ARCTAN -- Arctan Error (2)."""

    AVG: int = 3
    """AVG -- Average Error (3)."""


class Loss(LossMode):
    """Loss.
    """

    # def __init__(self, loss_mode: int, loss_limit: float) -> None:
    #     self._loss_mode: int = Loss.__check_mode(loss_mode)
    #     self._loss_limit: float = Loss.__check_limit(loss_limit)

    _loss_mode: int = LossMode.MSE
    _loss_limit: float = 0.1e-6

    @property
    def loss_mode(self) -> int:
        """The mode of calculation of the total error."""
        return self._loss_mode

    @loss_mode.setter
    def loss_mode(self, value: int) -> None:
        self._loss_mode = Loss.__check_mode(value)

    @classmethod
    def __check_mode(cls, value: int) -> int:
        return cls.MSE if cls.MSE > value > cls.AVG else value

    @property
    def loss_limit(self) -> float:
        """Minimum (sufficient) limit of the average of the error during training."""
        return self._loss_limit

    @loss_limit.setter
    def loss_limit(self, value: float) -> None:
        self._loss_limit = Loss.__check_limit(value)

    @staticmethod
    def __check_limit(value: float) -> float:
        return 0.1e-6 if value <= 0 else value


_TargetType = Callable[[], Union[Iterable[float], float]]
_InnerType = Callable[[], float]
_OuterType = Callable[[_TargetType], _InnerType]


def total_loss(mode: int = Loss.MSE) -> _OuterType:
    def outer(func: _TargetType) -> _InnerType:
        def inner() -> float:
            _loss = 0.0
            miss = func()

            if isinstance(miss, Iterable):
                count = 0.0
                for value in miss:
                    _loss += __get_loss(value, mode)
                    count += 1

                if count > 1:
                    _loss /= count
            elif isinstance(miss, float):
                _loss += __get_loss(miss, mode)

            if mode == Loss.RMSE:
                _loss = math.sqrt(_loss)

            if math.isnan(_loss):
                raise ValueError(f'{__name__}: loss not-a-number value')

            if math.isinf(_loss):
                raise ValueError(f'{__name__}: loss is infinity')

            return _loss

        return inner

    return outer


def __get_loss(value: float, mode: int) -> float:
    match mode:
        case Loss.AVG:
            return math.fabs(value)
        case Loss.ARCTAN:
            return math.atan(value) ** 2
        case Loss.MSE | Loss.RMSE | _:
            return value ** 2

# @total_loss(3)
# def calc_loss() -> Iterable[float]:
#     #for value in (0.27, -0.31, -0.52, 0.66, 0.81):
#     for value in (0.1, 0.2, 0.3, 0.4):
#         yield value
#
#
# @total_loss(2)
# def _calc_loss() -> float:
#     return 0.333
#
#
# if __name__ == "__main__":
#     print('calc_loss', calc_loss())
#     print('_calc_loss', _calc_loss())
