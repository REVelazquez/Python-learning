import numpy as np

# ----------------------- Arrays NumPy ----------------------- 

#   Numpy tiene como recurso principal su objeto array n-dimensional, el ndarry, que puede ser entendido como una colección de "ítems" 
# del mismo tipo. Este objeto funciona como un contenedor multidimensional que permite la realización de opreaciones matemáticas de forma
# rápida, simple y en grandes conjuntos de datos.

#   Los objetos ndarray presentan algunos atributos, como shape y dtype. Shape retorna una tupla con el tamaño de cada dimension del array
# y el atributo dtype retorna el tipo de dato del array.

# Otra característica de los arrays NumPy es que son homogéneos, es decir, solo pueden almacenar un tip ode dato.

# ----------------------- Creando arrays NumPy ----------------------- 

#   La forma más básica de creación de arrays NumPy es con la utilización de la función array(). Esta función puede ser utilizada para convertir
# otras estructuras de Python, como listas y tuplas, en arrays NumPy. En verdad la función array() acepta como argumento cualquier tipo de secuencia
# Python, inclusive otros arrays.

# --------------- Creando arrays a partir de secuencias --------------- 

#   Veamos algunos ejemplos de cómo son realizadas las conversiones de secuencias Python en arrays NumPy con el uso de la función array().

lista = [1000, 2300, 4987, 1500]
array = np.array(lista)
print (array)

# Utilizando tuplas tendremos el mismo resultado

tupla = [1000, 2300, 4987, 1500]
array2 = np.array(tupla)
print(array2)

#   Consultando el atributo shape del array creado en los trechos de código anteriores tenemos el siguiente resultado:
print(array.shape)

