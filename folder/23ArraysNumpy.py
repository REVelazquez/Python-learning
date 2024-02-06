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

# Indicando esto que se trata de un array unidimensional y que esta dimensión única tiene tamaño 4. Otro atributo importante es el dtype.
# Este nos devolvera el tipo de dato almacenado en el array

print(array.dtype)

#   En este caso no informamos explícitamente para la función array() el tipo de dato del array. Eso puede ser hecho con el argumento opcional
# dtype. Cuando este no es pasado, la funcion array() intentará inferir  el mejor tipo de dato para posibilitar la creación del array.

# -------------- Creando arrays a partir de datos externos --------------

#   Numpy, con el uso de la funcion loadtxt(), posibilita que sean creados arrays a paritr de archivos externos, como por ejemplo, cargar las
# informaciones de un archivo con extensión TXT y crear un array NumPy con este contenido. Suponga el siguiente contenido para el archivo
# "archivo.txt"

# 0
# 1
# 2
# 3
# 4

#   Para cargar el contenido de este archivo en un array Numpy basta utilizar la funcion loadtxt() de la siguiente forma:

"np.loadtxt(fname='archivo.txt)"

#   Con esto obtendremos un lo siguiente:
"array([0., 1., 2., 3., 4.])"

#   Hay que observar que en el archivo TXT, tendremos n'umeros enteros y, luego, en la importacion de su contenido en un array NumPy tenemos como
# resultado un array con dtype('float64). Esto pasa porque el argumento de la dtype de la función loadtxt() tiene como configuracion default el valor
# "float". Para modificar eso basta declarar explícitamente un valor diferente para el argumento dtype:

"si no fuera un sting esto y lo anterior seria:"
"np.loadtxt(fname= 'archivo.txt', dtype=int)"

#   Siguiendo con los arrays unidimensionales, considera el mismo contenido del archivo TXT anterior, pero ahora con una organización diferente:

"La organizacion seria: 0 1 2 3 4"

#   La utilización de la función loadtxt() con el contenido de este archivo genera ek mismo resultado obtenido anteriormente, o sea, un array NumPy unidimensional.

"np.loadtxt(fname='archivo.txt', dtype=int)"

# lo que nos devolvera:
"array([0, 1, 2, 3, 4])"

# Ahora crearemos un array bidimensional, con la funcion loadtxt(). veamos el siguiente archivo TXT:

"0 1"
"2 3"
"4 5"
"6 7"
"8 9"

#   Para generar un array bidimensional, con la funcion loadtxt(), cada línea en el archivo de texto debe tener el mismo número de valores.
array_txt = np.loadtxt(fname='archivo.txt', dtype= int)
print(array_txt)

#   Consultando el atributo shape de este array nos dara: (5, 2)

print(array_txt.shape)

#   El tamaño de la tupla indica elnúmero de dimensiones del array(dos) y los valores indican el tamaño de cada dimensión. Para facilitar 
# el entendimiento, en el ejempl ode arriba tenemos un array con 5 líneas y 2 columnas de datos.

#   Una característica común de los tres archivos de texto utilizados como ejemplo es que los valores numéricos dentro de cada uno están separados 
# por un espacio en blanco. El mismo es el carácter utilizado como delimitador default de la función loadtxt(). Cuando haya que asumir otro tipo de
# delimitador basta configurar el argumento delimiter, como en el siguiente ejemplo.

"1; 2; 3"
"4; 5; 6"
"7; 8; 9"
"10; 11; 12"
"13; 14; 15"

array_txt2=np.loadtxt(fname='archivo2.txt', delimiter= ';', dtype= int)
print(array_txt2)
