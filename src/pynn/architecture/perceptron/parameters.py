# from asyncio import Lock
# from typing import Optional


class Neuron:
    def __init__(self, value: float, miss: float) -> None:
        self.value = value
        self.miss = miss


class Parameters:
    """Parameters.
    """

    # Neurons
    neurons: list[list[Neuron]]

    # Transfer data
    data_weight: list[list[list[float]]]
    data_input: list[float]
    data_target: list[float]
    data_output: list[float]

    # Settings
    len_input: int = 55
    len_output: int
    last_layer_ind: int

    # def __init__(self) -> None:
    #     # Neurons
    #     self.neurons: list[list[Neuron]]
    #
    #     # Transfer data
    #     self.data_weight: list[list[list[float]]]
    #     self.data_input: list[float]
    #     self.data_target: list[float]
    #     self.data_output: list[float]
    #
    #     # Settings
    #     self.len_input: int
    #     self.len_output: int
    #     self.last_layer_ind: int
    #     self.is_init: bool = False
    #     self.config: Optional[str] = None
    #     self.mutex: Lock
