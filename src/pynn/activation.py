import math

from enum import IntEnum


class Mode(IntEnum):
    """Activation function mode."""

    """LINEAR - Linear/identity."""
    LINEAR = 0

    """RELU - ReLu (rectified linear unit)."""
    RELU = 1

    """LEAKY_RELU - Leaky ReLu (leaky rectified linear unit)."""
    LEAKY_RELU = 2

    """SIGMOID - Logistic, a.k.a. sigmoid or soft step."""
    SIGMOID = 3

    """TANH - TanH (hyperbolic tangent)."""
    TANH = 4


def check_activation_mode(mode: int) -> int:
    """Check activation mode."""
    return Mode.SIGMOID if mode > Mode.TANH else mode


def activation(value: float, mode: int = Mode.SIGMOID) -> float:
    """Activation function."""
    match mode:
        case Mode.LINEAR:
            return value
        case Mode.RELU:
            return .0 if value < 0 else value
        case Mode.LEAKY_RELU:
            return .01 * value if value < 0 else value
        case Mode.SIGMOID:
            return 1 / (1 + math.exp(-value))
        case Mode.TANH:
            value = math.exp(2 * value)
            return (value - 1) / (value + 1)
        case _:
            return -1


def derivative(value: float, mode: int = Mode.SIGMOID) -> float:
    """Derivative activation function."""
    match mode:
        case Mode.LINEAR:
            return 1
        case Mode.RELU:
            return 0 if value < 0 else 1
        case Mode.LEAKY_RELU:
            return .01 if value < 0 else 1
        case Mode.SIGMOID:
            return value * (1 - value)
        case Mode.TANH:
            return 1 - value ** 2
        case _:
            return -1


print(activation(value=.5, mode=Mode.TANH))
