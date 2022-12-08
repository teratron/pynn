import json
import os.path as path

from .hopfield.hopfield import Hopfield
from .perceptron.perceptron import Perceptron


def get(reader: str, **kwargs) -> Perceptron | Hopfield | OSError:
    """
    Returns an instance of one of the architectures or an error
    """
    if reader.lower() == Perceptron.name:
        return Perceptron(**kwargs)
    elif reader.lower() == Hopfield.name:
        return Hopfield(**kwargs)
    else:
        filename = path.normpath(reader)
        if path.isfile(filename):
            _, extension = path.splitext(filename)
            if extension == '.json':
                print('extension:', extension)
                with open(filename) as handle:
                    print(handle, json.load(handle)['name'])

            else:
                return FileExistsError('TODO:')
        else:
            print('json stream')

    return Perceptron(**kwargs)


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
