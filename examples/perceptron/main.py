# import time

from src.pynn.pynn import Pynn

if __name__ == '__main__':
    """
    New returns a new neural network
    instance with the default parameters
    for Hopfield neural network.
    """
    # pn = Pynn(
    #     bias=True,
    #     hidden_layers=[1],
    #     activation_mode=0,
    #     loss_mode=0,
    #     loss_limit=.01,
    #     rate=0.8)
    pn = Pynn(rate=0.8,
              activation_mode=Pynn.TANH,
              hidden_layers=[1, 2, 3])
    pn.query([.1, .2])
    print(pn.hidden_layers, pn.rate, pn.loss_limit)
    pn.rate = 0.73
    print(pn, pn.rate, Pynn.TANH, Pynn.RMSE)

    # print(pn.weight)
    pn.calc_neurons()
    # print(pn.weight)
    print(pn)

    # for i in range(10, -1, -1):
    #     print(i)
# New returns a new neural network
# instance with the default parameters,
# same n = nn.New("perceptron").
# n = nn.New()
#
# # The neuron bias, false or true.
# n.set_bias(True)
#
# # Array of the number of neurons in each hidden layer.
# n.set_hidden_layer(5, 3)
#
# # ActivationMode function mode.
# n.set_activation_mode(pynn.TANH)
#
# # The mode of calculation of the total error.
# n.set_loss_mode(pynn.MSE)
#
# # Minimum (sufficient) limit of the average of the error during training.
# lossLimit = 1e-6
# n.set_loss_limit(lossLimit)
#
# # Learning coefficient (greater than 0 and less than or equal to 1).
# n.set_rate(.3)
#
# # Dataset.
# dataset = {.27, -.31, -.52, .66, .81, -.13, .2, .49, .11, -.73, .28}
# len_data_input = 3  # Number of data_input data.
# len_data_output = 2  # Number of data_output data.
#
# start = time.time()
#
# # Training.
# len_data = len(dataset) - len_data_output
# for epoch in range(1, 10001):
#     for i in range(len_data_input, len_data + 1):
#         _, _ = n.Train(dataset[i - len_data_input:i], dataset[i:i + len_data_output])
#
#     # Verifying.
#     _sum, _num = 0, 0
#     for i in range(len_data_input, len_data + 1):
#         _sum += n.verify(dataset[i - len_data_input:i], dataset[i:i + len_data_output])
#         _num += 1
#
#     # Average error for the entire epoch.
#     # Exiting the cycle of learning epochs, when the minimum error level is reached.
#     if _sum / _num < lossLimit:
#         break
#
# print(f"Elapsed time: {time.time() - start}\n")
#
# # Writing the neural network configuration to a file.
# _ = n.write_config("perceptron.json")
#
# # Writing weights to a file.
# _ = n.write_weight("perceptron_weights.json")
#
# # Check the trained data, the result should be about [-0.13 0.2].
# print(n.query({-.52, .66, .81}))
