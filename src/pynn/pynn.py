from .perceptron.perceptron import Perceptron


# class Test(object):
#     def __new__(cls, **kwargs):
#         # instance = Perceptron()
#         instance = super().__new__(Perceptron)
#         instance.__init__(**kwargs)
#         print(instance, "566", cls.__class__, cls.__base__, cls.__mro__)
#         return instance


class Pynn(Perceptron):
    """
    Pynn.
    """

    def __new__(cls, **kwargs):
        instance = super().__new__(Perceptron)
        instance.__init__(**kwargs)
        return instance

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #
    #     print("567", self.__class__)
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
