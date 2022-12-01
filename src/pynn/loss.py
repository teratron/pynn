from enum import IntEnum


class Mode(IntEnum):
    """The mode of calculation of the total error."""

    """MSE - Mean Squared Error."""
    MSE = 0

    """RMSE - Root Mean Squared Error."""
    RMSE = 1

    """ARCTAN - Arctan Error."""
    ARCTAN = 2

    """AVG - Average Error."""
    AVG = 3


def check_loss_mode(mode: int) -> int:
    """Check loss mode."""
    return Mode.MSE if mode > Mode.AVG else mode
