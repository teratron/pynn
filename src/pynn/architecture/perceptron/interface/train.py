from typing import Any

from pynn.architecture.perceptron.perceptron import Perceptron


def train(obj: Perceptron, *args: Any, **kwargs: Any) -> tuple[int, float]:
    print(obj, args, kwargs)
    return 0, 0.1


def and_train(obj: Perceptron, *args: Any, **kwargs: Any) -> tuple[int, float]:
    print(obj, args, kwargs)
    return 0, 0.1

# // MaxIteration the maximum number of iterations after which training is forcibly terminated.
# const MaxIteration int = 1e+06
#
# var GetMaxIteration = getMaxIteration
#
# func getMaxIteration() int {
# 	return MaxIteration
# }
#
# // Train training dataset.
# func (nn *NN) Train(input []float64, target ...[]float64) (count int, loss float64) {
# 	var err error
# 	if len(input) > 0 {
# 		if len(target) > 0 && len(target[0]) > 0 {
# 			nn.mutex.Lock()
# 			defer nn.mutex.Unlock()
#
# 			if !nn.isInit {
# 				nn.Init(len(input), len(target[0]))
# 			} else {
# 				if nn.lenInput != len(input) {
# 					err = fmt.Errorf("invalid number of elements in the input data")
# 					goto ERROR
# 				}
# 				if nn.lenOutput != len(target[0]) {
# 					err = fmt.Errorf("invalid number of elements in the target data")
# 					goto ERROR
# 				}
# 			}
#
# 			if nn.Weights[0][0][0] != 0 {
# 				nn.weights = nn.Weights
# 			}
#
# 			nn.input = pkg.ToFloat1Type(input)
# 			nn.target = pkg.ToFloat1Type(target[0])
#
# 			minLoss := 1.
# 			minCount := 0
# 			for count < GetMaxIteration() {
# 				count++
# 				nn.calcNeuron()
#
# 				if loss = nn.calcLoss(); loss < minLoss {
# 					minLoss = loss
# 					minCount = count
# 					nn.Weights = nn.weights
# 					if loss < nn.LossLimit {
# 						return minCount, minLoss
# 					}
# 				}
# 				nn.calcMiss()
# 				nn.updateWeight()
# 			}
# 			return minCount, minLoss
# 		} else {
# 			err = pkg.ErrNoTarget
# 		}
# 	} else {
# 		err = pkg.ErrNoInput
# 	}
#
# ERROR:
# 	log.Printf("perceptron.NN.Train: %v\n", err)
# 	return 0, -1
# }
#
# // AndTrain the training dataset after the query.
# func (nn *NN) AndTrain(target []float64) (count int, loss float64) {
# 	var err error
# 	if len(target) > 0 {
# 		nn.mutex.Lock()
# 		defer nn.mutex.Unlock()
#
# 		if !nn.isInit {
# 			err = pkg.ErrInit
# 			goto ERROR
# 		} else if nn.lenOutput != len(target) {
# 			err = fmt.Errorf("invalid number of elements in the target data")
# 			goto ERROR
# 		}
#
# 		if nn.Weights[0][0][0] != 0 {
# 			nn.weights = nn.Weights
# 		}
#
# 		nn.target = pkg.ToFloat1Type(target)
#
# 		isStart := true
# 		minLoss := 1.
# 		minCount := 0
# 		for count < GetMaxIteration() {
# 			count++
# 			if !isStart {
# 				nn.calcNeuron()
# 			} else {
# 				isStart = false
# 			}
#
# 			if loss = nn.calcLoss(); loss < minLoss {
# 				minLoss = loss
# 				minCount = count
# 				nn.Weights = nn.weights
# 				if loss < nn.LossLimit {
# 					return minCount, minLoss
# 				}
# 			}
# 			nn.calcMiss()
# 			nn.updateWeight()
# 		}
# 		return minCount, minLoss
# 	} else {
# 		err = pkg.ErrNoTarget
# 	}
#
# ERROR:
# 	log.Printf("perceptron.NN.AndTrain: %v\n", err)
# 	return 0, -1
# }
