import pynn

# New returns a new neural network
# instance with the default parameters
# for Hopfield neural network.
n = pynn.new("hopfield")
n.set_energy(.1)
print("pynn.new('hopfield'):", n)
