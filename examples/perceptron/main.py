import time

from src.pynn.pynn import Pynn

if __name__ == '__main__':
    # Returns a new neural network
    # instance with the default parameters
    # for Perceptron neural network.
    """
    p = Pynn()
    p = Pynn('perceptron')
    p = Pynn('config/perceptron.json')
    p = Pynn("{name: 'perceptron'}")
    """
    pn = Pynn('perceptron',
              bias=True,
              hidden_layers=[5, 3],
              activation_mode=Pynn.TANH,
              loss_mode=Pynn.MSE,
              loss_limit=1e-6,
              rate=.3)

    pn.query([.1, .2])
    pn.rate = 0.73
    print(pn.rate, pn.TANH, pn.RMSE)
    pn.calc_neurons()

    # Dataset.
    # dataset = {.27, -.31, -.52, .66, .81, -.13, .2, .49, .11, -.73, .28}
    # len_data_input = 3  # Number of data_input data.
    # len_data_output = 2  # Number of data_output data.

    start = time.time()

    # Training.
    # len_data = len(dataset) - len_data_output
    # for epoch in range(1, 10001):
    #     for i in range(len_data_input, len_data + 1):
    #         _, _ = pn.train(dataset[i - len_data_input:i], dataset[i:i + len_data_output])
    #
    #     # Verifying.
    #     _sum, _num = 0, 0
    #     for i in range(len_data_input, len_data + 1):
    #         _sum += pn.verify(dataset[i - len_data_input:i], dataset[i:i + len_data_output])
    #         _num += 1
    #
    #     # Average error for the entire epoch.
    #     # Exiting the cycle of learning epochs, when the minimum error level is reached.
    #     if _sum / _num < loss_limit:
    #         break

    print(f"Elapsed time: {time.time() - start}\n")

    # # Writing the neural network configuration to a file.
    # _ = pn.write_config("perceptron.json")
    #
    # # Writing weights to a file.
    # _ = pn.write_weights("perceptron_weights.json")
    #
    # # Check the trained data, the result should be about [-0.13 0.2].
    # print(pn.query({-.52, .66, .81}))
