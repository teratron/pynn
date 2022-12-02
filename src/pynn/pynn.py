from .perceptron import Perceptron


class Pynn(Perceptron):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # def __init__(self,
    #              bias,
    #              hidden_layer,
    #              activation_mode,
    #              loss_mode,
    #              loss_limit,
    #              rate):
    # self.bias = bias
    # self.hidden_layer = hidden_layer,
    # self.activation_mode = activation_mode,
    # self.loss_mode = loss_mode,
    # self.loss_limit = loss_limit,
    # self.rate = rate

    # super().__init__(
    #     bias,
    #     hidden_layer,
    #     activation_mode,
    #     loss_mode,
    #     loss_limit,
    #     rate)

    # def __call__(self, *args, **kwargs):
    #     print()
    #     pass
