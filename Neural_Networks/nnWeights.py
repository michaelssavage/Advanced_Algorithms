"""
This time return both weights. You should see the numpy random generator just once, 
before creating the W1. Then create W2. Return both weights.

As before, the neural network class constructor is defined as follows:

import numpy as np
class NeuralNetwork(object):
   def __init__(self, size_input, size_hidden, size_output):
       np.random.seed(x)
       self.W1 = np.random.randn(size_input, size_hidden)
       self.W2 = np.random.randn(size_hidden, size_output)

NN = NeuralNetwork(2, 3, 1)
"""
import numpy as np
class NeuralNetwork(object):
   def __init__(self, size_input, size_hidden, size_output):
       self.W1 = np.random.randn(size_input, size_hidden)
       self.W2 = np.random.randn(size_hidden, size_output)


def main():
	np.random.seed(152)
	NN = NeuralNetwork(2, 3, 1)
	print(NN.W1,NN.W2)

if __name__ == "__main__":
    main()
