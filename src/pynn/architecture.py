import json
import os.path as path
from typing import Union

from .hopfield.hopfield import Hopfield
from .perceptron.perceptron import Perceptron


def get(reader: str, **kwargs) -> Union[Perceptron, Hopfield, Exception]:
    """
    Returns an instance of one of the architectures or an error.
    """
    if reader.lower() == Perceptron.name:
        return Perceptron(**kwargs)
    elif reader.lower() == Hopfield.name:
        return Hopfield(**kwargs)
    else:
        data: dict
        filename = path.normpath(reader)
        if path.isfile(filename):
            _, extension = path.splitext(filename)
            if extension == '.json':
                with open(filename) as handle:
                    data = json.load(handle)
                data['config'] = filename
            else:
                return FileExistsError('TODO:')
        else:
            data = json.loads(reader)
            data['config'] = None

        if 'name' in data:
            return get(data['name'], **data)

    return Perceptron()

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
