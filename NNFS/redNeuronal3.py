import numpy as np

inputs = [1, 2, 3, 2.5] 
#Esto es un vector
# Los weights que antes eran diferentes listas ahora son una sola, es decir una lista anidada
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]
# Esto es una matriz de vectores
# Lo mismo ocurre con las bias
biases= [2, 3, 0.5]
# Esto es un vector
# De esta forma simplificamos el codigo que teniamos anteriormente

# Los weights y bias: cambian la magnitud o cambian el offset de un valor

# Hay que recordar que es la forma y tipo de un array, es decir lineas, columnas etc

# Los tensores son objetos que se pueden representar como un array

# Lo que queremos ahora es aplicar que el primer vector se multiplique por el segunda, es decir que ocurra el
# producto de punto, llamado asi cuando se trabaja en vectores.

# En este caso no importa cual de los dos va primero, pero sin embargo mas adelante si va a importar
# output = np.dot(weights, inputs) + bias tener en cuenta que esto ocurre cuando los pesos y bias son solo uno o de una dimension.
# en este caso estamos haciendo que output sea:
# output = 0.2*1.0 + 0.8*2.0+ -0.5*3.0 + 1.0 * 2.5 = 2.8 y luego sumamos la bias, que seria: 2.8+2, dandonos 4.8
# print(output)


# Ahora se vera porque los pesos van antes que los inputs
output = np.dot(weights, inputs) +biases
# Como son tres "sets" de weights sabemos que son tres neuronas, es por ello que primero pasamos los pesos.
# ademas si utilizamos primero inputs en la multiplicación nos dara un error
# Lo que ocurre aqui es que se aplica la funcion "dot" tres veces, haciendo asi lo siguiente:
# np.dot(weights[0], inputs), np.dot(weights[1], inputs), np.dot(weights[2], inputs)
# que da de resultado: [2.8, -1.79, 1.885] y luego a este resultado se suma las biases, es decir
#  [2.8, -1.79, 1.885] + [2, 3, 0.5], dando como resultado [4.8   1.21  2.385]

print(output)