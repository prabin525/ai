# Three layer neural network for XOR 

import numpy as np


alphas = [0.001,0.01,0.1,1,10,100,1000]
hiddenSize = 16
#alphas = [10]

#Sigmoid function
def sigmoid(x):
	output = 1/(1+np.exp(-x))
	return output

#Derivative of the Sigmoid Function
def sigmoid_derivative(output):
	return output*(1-output)

#Input Dataset
x = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
#x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])


#Output Dataset
y = np.array([[0,1,1,0,1,0,0,1]]).T
#y = np.array([[0],[1],[1],[0]])


for alpha in alphas:
	print("Training with Alpha: "+str(alpha))
	#Seed to generate the same random all the times
	np.random.seed(1)

	#random weight for the two layers
	syn0 = 2*np.random.random((3,hiddenSize)) - 1
	syn1 = 2*np.random.random((hiddenSize,1)) - 1

	for iter in range(60000):

		#forward Progpagation

		l0 = x
		l1 = sigmoid(np.dot(l0,syn0))
		l2 = sigmoid(np.dot(l1,syn1))

		#error in the output layer
		l2_error = l2-y
		if (iter% 10000) == 0:
			print ("Error after "+str(iter)+" iterations:" + str(np.mean(np.abs(l2_error))))

		l2_delta = l2_error * sigmoid_derivative(l2)
 	
		#backpropagate the error
		l1_error = l2_delta.dot(syn1.T)

		l1_delta = l1_error * sigmoid_derivative(l1)

		syn1 -= alpha * l1.T.dot(l2_delta)
		syn0 -= alpha * l0.T.dot(l1_delta)

if __name__ == '__main__':
	print('Training Input X')
	print(x)
	print('Training Output Y')
	print(y)
	print('output after training')
	print(l0)
	print(l1)
	print(l2)
	print('Input ')
	a = np.array([1,0,1])
	print (a)
	print('output')
	b = np.around(sigmoid(np.dot((sigmoid(np.dot(a,syn0))),syn1)))
	print(b)
