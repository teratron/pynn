from pynn import NeuralNetwork


class Hopfield(NeuralNetwork):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def info(self):
        print('hopfield')