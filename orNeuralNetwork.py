#Input and Output layer based OR Neural Networ,no hidden network


import numpy as np

#Sigmoid function
def sigmoid(x):
	output = 1/(1+np.exp(-x))
	return output

#Derivative of the Sigmoid Function
def sigmoid_derivative(output):
	return output*(1-output)

#Input Dataset
x = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])

#Output Dataset
y = np.array([[0,1,1,1,1,1,1,1]]).T

#Seed to generate the same random all the times
np.random.seed(1)

# random wieght for the layer
syn0 = 2*np.random.random((3,1)) - 1

for iter in range(10000):

	#forward propagation
	l0 = x
	l1 = sigmoid(np.dot(l0,syn0))
	
	#error
	l1_error = y - l1

	#backpropaget the error
	l1_delta = l1_error * sigmoid_derivative(l1)


	#update the weights
	syn0 += np.dot(l0.T, l1_delta)

if __name__ == '__main__':
	print('Training Input X')
	print(x)
	print('Training Output Y')
	print(y)
	print('output after training')
	print(l1)
	print('Input ')
	a = np.array([1,0,1])
	print (a)
	print('output')
	b = np.around(sigmoid(np.dot(a,syn0)))
	print(b)