from typing import Any


def query(obj: object, *args: Any, **kwargs: Any) -> list[float]:
    print("query***:", obj, args, kwargs)
    # obj.calc_neurons()
    return [0, 1]


"""
// Query querying dataset.
func (nn *NN) Query(input []float64) []float64 {
	var err error
	if len(input) > 0 {
		nn.mutex.Lock()
		defer nn.mutex.Unlock()

		if !nn.isInit {
			err = pkg.ErrInit
			goto ERROR
		} else if nn.lenInput != len(input) {
			err = fmt.Errorf("invalid number of elements in the input data")
			goto ERROR
		}

		if nn.Weight[0][0][0] != 0 {
			nn.weight = nn.Weight
		}

		nn.input = pkg.ToFloat1Type(input)

		nn.calcNeuron()
		for i, n := range nn.neuron[nn.lastLayerIndex] {
			nn.output[i] = float64(n.value)
		}
		return nn.output
	} else {
		err = pkg.ErrNoInput
	}

ERROR:
	log.Printf("perceptron.NN.Query: %v\n", err)
	return nil
}
"""
