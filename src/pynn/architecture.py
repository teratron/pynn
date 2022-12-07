import os.path as path

from .hopfield.hopfield import Hopfield
from .perceptron.perceptron import Perceptron


def get(reader: str) -> Perceptron | Hopfield | OSError:
    """
    get_architecture
    """
    if reader.lower() == Perceptron.name:
        return Perceptron()
    elif reader.lower() == Hopfield.name:
        return Hopfield()
    else:
        filename = path.normpath(reader)
        if path.isfile(filename):
            _, extension = path.splitext(filename)
            if extension == '.json':
                print('')
            else:
                return FileExistsError('TODO:')

    return Hopfield()


a = get('PERCEPTRON')
print(a)

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
