class Parameters:
    """
    Parameters.
    """

    def __init__(self) -> None:
        # Neurons, type: list[list[Neuron]]
        self.neurons = None  # [[Neuron(-.5, 0) for _ in range(3)] for _ in range(2)]

        # Transfer data
        self.data_weight = self.weights
        self.data_input = [.1, .3]  # TODO:
        self.data_target = [.1, .3]  # TODO:
        self.data_output = [.1, .3]  # TODO:

        # Settings
        self.len_input = 2  # TODO:
        self.len_output = 2  # TODO:
        self.last_layer_ind = 1  # TODO:
        self.is_init = False  # TODO:
        # self.mutex: sync.Mutex  # TODO:
