import numpy as np
import nnfs
nnfs.init() # Esta es una herramienta que ayuda para aprender. Nos provee un data set para poder hacerllo
from nnfs.datasets import spiral_data


X = [[    1,   2,    3,  2.5],
     [  2.0, 5.0, -1.0,  2.0],
     [ -1.5, 2.7,  3.3, -0.8]] 

X, y = spiral_data(100, 3)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10*np.random.randn(n_inputs, n_neurons)

        self.biases = np.zeros((1, n_neurons))
        
    def forward(self, inputs):
        self.output= np.dot(inputs, self.weights)+self.biases
# Luego de hacer todo esto vendria la funcion de activacion.
# Los pasos siguientes a las funciones de activacion es la "perdida" o el calculo de la misma, por ello es necesario una funcion de activacion
# para asi saber que tan cerca estamos de que haya un cero o un uno.
# Hay diferentes tipos, sigmoidales, lineales etc. En las lineales los valores nunca van a ser menores a ceros, mientras en las otras si pueden tomar esos valores.
# a las lineales las usaremos proque son rapidas, mientras que las sigmoidales son un poco mas complejas a las lineales, por ende son relativamente mas lentas.
# En el caso de las funciones lineales necesitamos usar siempre funciones lineales. Ya que cuando queremos hacer que los valores de una funcion que no sea lineal
# se relacionen con las lineales es imposible. Por eso usamos Rectificaciones Lineales para ello, ya que si bien no es perfecta, en el caso de un funcionamiento sigmoideal,
# es muy similar.
class Activation_ReLu:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

       

layer1= Layer_Dense(2, 5)
activation1 = Activation_ReLu()

layer1.forward(X)
activation1.forward(layer1.output)
print(activation1.output)
