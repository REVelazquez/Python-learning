
import numpy as np
# Lotes: a mas lotes de info mas precisa sera nustra neurona/capa de calculo

inputs = [
    [    1,   2,    3,  2.5],
    [  2.0, 5.0, -1.0,  2.0],
    [ -1.5, 2.7,  3.3, -0.8]] 

weights = [
    [  0.2,   0.8, -0.5,  1.0],
    [  0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]]

biases= [2, 3, 0.5]

# Al tener la misma forma los inputs y pesos, se genera un error para salvar el mismo
# debemos cambiar columnas por filas, es decir transponer los pesos.

output = np.dot(inputs, np.array(weights).T) +biases
print(output) 