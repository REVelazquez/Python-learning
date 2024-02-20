import numpy as np

# ------------- Atributos ------------- 

#   Los atributos de un array posibilitan acceder a informaciones intrínsecas del mismo. En esta sección vamos a conocer los principales
# atributos de los arrays NumPy.

#   Para ayudar en los ejemplos considere los arrays "letras", "numeros" y "datos":

letras = np.array(['A', 'B', 'C', 'D', 'E'])
numeros= np.arange(1, 6)
datos = np.array([letras, numeros])

print(datos) #Nos devuelve lo siguiente
# [['A' 'B' 'C' 'D' 'E']
#  ['1' '2' '3' '4' '5']]

# ------------- ndarray.shape ------------- 

#   Retorna una tupla con las dimensiones del array. Este atributo es utilizado para obtener la forma de un array, pero también puede ser
# utilizado para remodelar un array in-place, asinándole una tupla con las nuevas dimensiones

print(datos.shape) # nos devolvera (2, 5)

#   Como se vio en secciones anteriores, el resultado nos enseña que "datos" tiene dos dimensiones, la primera(eje 0 o líneas) tiene tamaño 2
# y la segunda dimensión(eje 1 o columnas) tiene tamaño 5

#   El procedimiento de ajuste de la dimensión utilizando la modificación del atributo shape necesita que la nueva tupla informada genere un array 
# con el mismo número de elementos del array de origen. Por ejemplo, "datos" tiene un shape igual a (2, 5), indicando que este array tiene un total
# de 10 elementos. De esta forma para remodelar el array datos utilizando "shap" será necesario un shape que garantice exactamente 10 elementos 
# para el nuevo formato.

datos.shape = (1, 10)

print(datos)
# Esto nos devuelve: [['A' 'B' 'C' 'D' 'E' '1' '2' '3' '4' '5']]

datos.shape = (5, 2)
print(datos)
# Esto nos devolverá:
# [['A' 'B']
# ['C' 'D']
# ['E' '1']
# ['2' '3']
# ['4' '5']]

datos.shape = (2, 5)
print(datos)
# Nuevamente nos retornará:
# [['A' 'B' 'C' 'D' 'E']
#  ['1' '2' '3' '4' '5']]

#  ------------- ndarray.ndim ------------- 
#   Retorna el número de dimensiones del array

print(datos.ndim) # Retornará 2

# ------------- ndarray.size ------------- 
#   Retorna el número de elementos del array
print(datos.size) # Retornará 10

#  ------------- ndarray.dtype ------------- 
#   Retorna el tipo de datos de los elementos del array

print(datos.dtype) # Retornará <U11

# ------------- ndarray.T
#   Retorna el array transpuesto, o sea, convierte líneas en columnas y viceversa. No modifica el array in-place.

print(datos.T) # Nos retornará:
# [['A' '1']
# ['B' '2']
# ['C' '3']
# ['D' '4']
# ['E' '5']]

print(datos) # Como se ve, aqui el array no sufrio cambios.

#   Podemos obtener el mismo resultado con el método transpose()

# ------------- Métodos ------------- 
