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
class Activation_Softmax:
    def forward(self, inputs):
        exp_values= np.exp(inputs - np.max(inputs, axis=1, keepdims= True))
        probabilities= exp_values / np.sum(exp_values, axis= 1, keepdims=True)
        self.output = probabilities

# Categorical cross-Entropy. Nos servira para calcular la perdida, en este caso usaremos logaritmo, debido a que este es una
# de las formas mas utilizadas.
# One-hot encoding es un vector que tiene n-clases de largo, donde estara llego de 0 ceros a excepcion de la clase a la que se esta apuntando.
# Generalmente cuando se usa el logaritmo en programacion se usa el logaritmo natural, es decir con base en el numero de Euler

class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_CategoricaLCrossEntropy(Loss):
    def forward(self, y_pred, y_true):
        # Y_true son los valores de entrenamiento y y_pred son los valores de la red neuronal
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        # Hay veces qeu la gente pasara valores como escalares o como inputs one hot codeados.
        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped*y_true, axis = 1)
        negative_log_likelihoods= -np.log(correct_confidences)
        return negative_log_likelihoods
    
X, y = spiral_data(samples = 100, classes = 3)

dense1 = Layer_Dense(2, 3)
activation1= Activation_ReLu()

dense2= Layer_Dense(3, 3)
activation2= Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

loss_function = Loss_CategoricaLCrossEntropy()
loss = loss_function.calculate(activation2.output, y)

print('Loss', loss)

