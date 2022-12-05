import logging
import math


def calc_loss(obj) -> float:
    # TODO: try-catch
    loss = 0.
    for i in range(obj.len_output):
        obj.neuron[obj.last_layer_ind][i].miss = obj.data_target[i] - obj.neuron[obj.last_layer_ind][i].value
        match obj.loss_mode:
            case obj.MSE, obj.RMSE, _:
                loss += obj.neuron[obj.last_layer_ind][i].miss ** 2
            case obj.ARCTAN:
                loss += math.atan(obj.neuron[obj.last_layer_ind][i].miss) ** 2
            case obj.AVG:
                loss += math.fabs(obj.neuron[obj.last_layer_ind][i].miss)

    loss /= obj.len_output
    if obj.loss_mode == obj.RMSE:
        loss = math.sqrt(loss)

    match True:
        case math.isnan(loss):
            logging.log(0, 'perceptron.calc_loss: loss not-a-number value')
        case math.isinf(loss):
            logging.log(0, 'perceptron.calc_loss: loss is infinity')

    return loss
