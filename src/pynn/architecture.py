import io
import json
import os.path as path
from typing import IO

from .hopfield.hopfield import Hopfield
from .perceptron.perceptron import Perceptron


class Config(io.TextIOWrapper):
    def __init__(self, name: str, buffer: IO[bytes]):
        super().__init__(buffer)


def get(reader: str, **props) -> Perceptron | Hopfield | OSError:
    """
    Returns an instance of one of the architectures or an error
    """
    if reader.lower() == Perceptron.name:
        return Perceptron(**props)
    elif reader.lower() == Hopfield.name:
        return Hopfield(**props)
    else:
        filename = path.normpath(reader)
        if path.isfile(filename):
            _, extension = path.splitext(filename)
            if extension == '.json':
                print('extension:', extension)
                conf: any
                with open(filename) as handle:
                    data = json.load(handle)
                    print(handle.buffer, data)
                    conf: type(handle) = handle
                    print(dict(conf.buffer))

            else:
                return FileExistsError('TODO:')
        else:
            print('json stream')

    return Perceptron(**props)


# print('get:', get('PERCEPTRON'))

"""
const (
	Perceptron = perceptron.Name
	Hopfield   = hopfield.Name
)

// Get.
func Get(reader string) pkg.NeuralNetwork {
	var err error
	r := utils.ReadFile(reader)
	if _, ok := r.(*utils.FileError); ok {
		switch strings.ToLower(reader) {
		case Perceptron:
			return perceptron.New()
		case Hopfield:
			return hopfield.New()
		default:
			err = fmt.Errorf("neural network is %w", pkg.ErrNotRecognized)
		}
	} else {
		switch v := r.GetValue("name").(type) {
		case error:
			err = v
		case string:
			if n := Get(v); n != nil {
				if err = r.Decode(n); err == nil {
					r.ClearData()
					n.Init(r)
					return n
				}
			}
		}
	}

	if err != nil {
		log.Printf("arch.Get: %v", err)
	}
	return nil
}
"""
