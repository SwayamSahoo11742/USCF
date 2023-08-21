import numpy as np

def sigmoid_trasnform(x):
	return 100 / (1 + np.exp(-0.1 * x)