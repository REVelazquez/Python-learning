import numpy as np
# Lotes: a mas lotes de info mas precisa sera nustra neurona/capa de calculo

# inputs = [
#     [    1,   2,    3,  2.5],
#     [  2.0, 5.0, -1.0,  2.0],
#     [ -1.5, 2.7,  3.3, -0.8]] 

# # Segunda capa
# weights = [
#     [  0.2,   0.8, -0.5,  1.0],
#     [  0.5, -0.91, 0.26, -0.5],
#     [-0.26, -0.27, 0.17, 0.87]]

# biases= [2, 3, 0.5]

# weights2 = [
#     [  0.1, -0.14, -0.5],
#     [ -0.5, 0.12, -0.33],
#     [-0.44, 0.73, -0.13]]

# biases2= [-1, 2, -0.5]

# # Al tener la misma forma los inputs y pesos, se genera un error para salvar el mismo
# # debemos cambiar columnas por filas, es decir transponer los pesos.

# layer1_outputs = np.dot(inputs, np.array(weights).T) +biases

# layer2_outputs= np.dot(layer1_outputs, np.array(weights2).T) +biases2

# print(layer2_outputs)

# Si bien esto se puede hacer la forma correcta de utilizarlo es asi:
np.random.seed(0)

# En machine learning generalmente la "X" es como se pone la data de entrenamiento
X = [[    1,   2,    3,  2.5],
     [  2.0, 5.0, -1.0,  2.0],
     [ -1.5, 2.7,  3.3, -0.8]] 

# Ahora definiremos las dos "capas escondidas". Les decimos asi porque de cambiar algo solo sera los inputs
# Para iniciar una red primero cargaremos un modelo, o lo cargaremos. Si iniciamos una nueva red necesitamos
# iniciar los pesos con valores qeu van de -1.0 a +1.0. Generalmente se busca valores pequeños porque queremos que
# los valores esten entre -1.0 y 1.0
# Cuando tenemos un conjunto de datos lo primero que queremos hacer es normalizarlo y luego escalarlo.
# Para las biases generalmente las iniciamos en 0 hay veces que no queremos hacerlo  porque hay veces que no nos otorga un valor
# y nos da un 0, por ende la red estara muerta por ello en esos casos se inicia en otro numero que no sea 0.


class Layer_Dense: # Cuando creemos esta capa especificaremos los valores que estan en init
    def __init__(self, n_inputs, n_neurons):
        # Aqui necesitamos la cantidad de inputs y la cantidad de neuronas que queremos. En este caso sera
        # Aqui los parametros seran la forma. "El 0.10 *" es para que los numeros esten entre -1 y 1
        self.weights = 0.10*np.random.randn(n_inputs, n_neurons)
        # Haciendo la forma de los pesos de esta forma no necesitamos transponer luego los mismos
        # En este caso necesitamos tantas "bias" como neuronas tendremos. Por ende debemos pasar la "forma" que queremos tenda luego

        self.biases = np.zeros((1, n_neurons))
        
    def foward(self, inputs):
        self.output= np.dot(inputs, self.weights)+self.biases
        
# En la siguiente parte lo primero es la cantidad de inputs que tenemos en un lote, es decir una fila, en este caso 4. Y el segundo parametro
# es cualquier numero que nosotros queramos ya que son las neuronas, pero para visualizarlo esta vez sera 5.

layer1= Layer_Dense(4, 5)
# En este caso tenemos que recordar que en la primera capa, es decir layer1, tendremos 5 lotes, por ende el primer parametro del layer2 debe ser 5,
# el segundo nuevamente puede ser cualquier numero que queramos.
layer2= Layer_Dense(5, 2)

layer1.foward(X)
# print(layer1.output)# Este output sera el input del layer 2
layer2.foward(layer1.output)

print(layer2.output)
