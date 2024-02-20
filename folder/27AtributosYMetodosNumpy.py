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

#   El objeto array de NumPy posee un conjunto amplio de métodos. Son usados para conversión, manipulación, cálculo, etc. A continuación conoceremos
# algunos de uso más común, dejando los métodos de calculo para luego.

# ------------- ndarray.tolist() ------------- 

#   Retorna una copia de los datos de un array como una lista de Python. Los datos son convertidos para el tipo de Python compatible.

print(datos.tolist()) 
# esto nos retornara[['A', 'B', 'C', 'D', 'E'], ['1', '2', '3', '4', '5']]

#   Como datos es un array bidimensional, el retorno del método es una lista anidada.

# ------------- ndarray.reshape(shape, order= 'C') ------------- 

#   Altera la forma de un array sin alterar sus datos. Considere el array contador a seguir para nustros ejemplos.

contador=np.arange(15)
print(contador)
# retorna: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

#   Para utilizar el método reshape() basta pasar como argumento el nuevo shape del array en formato de tupla o los elementos del shape como argumentos 
# separados

print(contador.reshape(5,3))
# Nos retorna:
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]
#  [12 13 14]]

#   La otra forma de escribirlo seria contador.reshape(5, 3)

#   Este método posee también el argomento order, que es opcional y define si los datos serán orientados a las líneas(orden C) o a las columnas(orden Fortran).
# Esto permite controlar la forma como los datos del array quedan organizados en la memoria. Arrays NumPy son creados, por patrón, en una orden orientadas a
# líneas y esta es la opción default del método reshape()

# ------------- ndarray.resize(new_shape, refcheck=True) ------------- 

#   Altera la forma y el tamaño del array in-place
#   Este método posee el argumento opcionar refcheck que es un booleano que indica si la verificación del conteo de referencia debe ser hecha o no. El objetivo
# es verificar si el buffer del array está relacionado a cualquier otro objeto. Por default es True

#   Sin embargo, los conteos de referencia pueden aumentar por otros motivos. Por tanto, si el array no comparte memoria con otro objeto Python, podrás definir 
# con seguridad el argumento refcheck como False, evitando así el error.

datos.resize((3,5), refcheck=False) # En este caso retornaria error si en vez de False seria True 
print(datos)
# esto nos retornará:
# [['A' 'B' 'C' 'D' 'E']
#  ['1' '2' '3' '4' '5']
#  ['' '' '' '' '']]

#   Hay que darse cuenta de que el códigp aumentó una de las dimensiones(Eje 0) del array datos y llenó este nuevo espacio con strings vacíos. Si el array original
# fuese llenado con datos numéricos el método los llenaría con ceros, si fuesen booleanos serían False.

contador = np.arange(10)
print(contador) # [0 1 2 3 4 5 6 7 8 9]

contador.resize((3,5), refcheck=False)
print(contador)
#   Esto nos da como resultado:
# [[0 1 2 3 4]
#  [5 6 7 8 9]
#  [0 0 0 0 0]]