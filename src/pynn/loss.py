class Mode:
    """The mode of calculation of the total error."""

    """MSE - Mean Squared Error."""
    MSE: int = 0

    """RMSE - Root Mean Squared Error."""
    RMSE: int = 1

    """ARCTAN - Arctan Error."""
    ARCTAN: int = 2

    """AVG - Average Error."""
    AVG: int = 3


def check(mode: int) -> int:
    """Check loss mode."""
    return Mode.MSE if mode > Mode.AVG else mode
