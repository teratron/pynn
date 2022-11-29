from src.pynn.pynn import Pynn

if __name__ == '__main__':
    """
    New returns a new neural network
    instance with the default parameters
    for Hopfield neural network.
    """
    pn = Pynn('perceptron')
    pn.query([.1, .2])

    print(pn.get_bias())

    # n.set_energy(.1)
    # print("nn.New('hopfield'):", pn)
