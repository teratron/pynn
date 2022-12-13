from asyncio import Lock


class Neuron:
    def __init__(self, value: float, miss: float) -> None:
        self.value = value
        self.miss = miss


class Parameters:
    """
    Parameters.
    """

    def __init__(self) -> None:
        # Neurons
        self.neurons: list[list[Neuron]]

        # Transfer data
        self.data_weight: list[list[list[float]]]
        self.data_input: list[float]
        self.data_target: list[float]
        self.data_output: list[float]

        # Settings
        self.len_input: int
        self.len_output: int
        self.last_layer_ind: int
        self.is_init: bool
        self.mutex: Lock
