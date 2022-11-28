from .perceptron.main import Perceptron


# from hopfield.main import Hopfield

# PERCEPTRON = Perceptron.name
# HOPFIELD = Hopfield.name


def get_architecture(name: str):
    print('arch:', name, Perceptron.name)
    # match name.lower():
    #     case Hopfield.name:
    #         return Hopfield()
    #
    # return Perceptron()


# a = get_architecture('PERCEPTRON')
# print(a.name)


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
