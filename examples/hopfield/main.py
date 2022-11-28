from src.pynn.pynn import Pynn

# from src import Pynn

if __name__ == '__main__':
    """
    New returns a new neural network
    instance with the default parameters
    for Hopfield neural network.
    """
    pn = Pynn('perceptron')
    pn.info()

    # n.set_energy(.1)
    # print("nn.New('hopfield'):", pn)
