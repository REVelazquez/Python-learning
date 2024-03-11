import numpy as np
import nnfs
nnfs.init()
from nnfs.datasets import spiral_data

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10*np.random.randn(n_inputs, n_neurons)

        self.biases = np.zeros((1, n_neurons))
        
    def forward(self, inputs):
        self.output= np.dot(inputs, self.weights)+self.biases

class Activation_ReLu:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

# Necesitamos  las activaciones softmax para cuando nuestra neurona funciona con una funcion de activacion lineal, ya que de esta forma
# estariamos otorgandole a un negativo un valor que nos daria un numero en positivo y no nos dejaria perder el "valor" de ese negativo como lo 
# haria una funcion de activacion lineal.
        
# Una vez que logramos hacer la exponenciacion para salvar el negativo debemos normalizar el valor que nos da dicha exponenciacion
# Softmax es la union de exponenciacion y normalizacion de valores

class Activation_Softmax:
    def forward(self, inputs):
        exp_values= np.exp(inputs - np.max(inputs, axis=1, keepdims= True))
        probabilities= exp_values / np.sum(exp_values, axis= 1, keepdims=True)
        self.output = probabilities

X, y = spiral_data(samples = 100, classes = 3)

dense1 = Layer_Dense(2, 3)
activation1= Activation_ReLu()

dense2= Layer_Dense(3, 3)
activation2= Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])