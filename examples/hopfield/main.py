from src.pynn import Pynn

if __name__ == '__main__':
    """
    New returns a new neural network
    instance with the default parameters
    for Hopfield neural network.
    """
    n = Pynn('hopfield')

    #n.set_energy(.1)
    print("nn.New('hopfield'):", n, end='sdsa')
