def calc_miss(obj) -> None:
    if obj.last_layer_ind > 0:
        for i in range(obj.last_layer_ind - 1, -1, -1):
            inc = i + 1
            for j in range(len(obj.neuron[i])):
                obj.neuron[i][j].miss = 0.
                for k, m in range(len(obj.neuron[inc])):
                    obj.neuron[i][j].miss += obj.neuron[inc][k].miss * obj.data_weight[inc][k][j]
