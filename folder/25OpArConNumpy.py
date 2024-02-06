import numpy as np
# ---------- Operaciones aritméticas con arrays numpy ---------- 

#   Un recurso importante en la utilizacion de los arrays Numpy es que se pueden hacer operaciones aritméticas rápidas sin utilizas ningún bucle "for". Veremos
# a continuacion la aplicación de este recurso en arrays de misma dimensión y en arrays de diferentes dimensiones(broadcasting)

# ---------- Operaciones aritméticas entre arrays de misma dimensión ---------- 

#   Operaciones aritméticas aplicadas entre arrays de misma dimensión serán replicadas para todos los elementos de estos arrays. Esa forma de cálculo es conocida
# como vectorización en la biblioteca NumPy y veremos algunos ejemplos utilizando arrays de una y dos dimensiones

# ---------- Arrays con una dimensión ---------- 
#   Vamos a suponer que estamos trabajando con informaciones sobre el mercado inmobiliario y necesitamos generar contenido con los datos que tenemos disponibles.
# Considere que tenemos las informaciones sobre el precio de venta de un conjunto de cinco inmuebles en una lista llamada "valor" y sus respectivas superficies
# (en m^2) en una lista llamada m2

valor = [450000, 1500000, 280000, 650000, 325000]
m2 = [90, 150, 70, 100, 65]

#   Una información interesante que puede ser retirada de estos dos datos es el valor del metro cuadrado por cada inmueble. Esta informacion es fácilmente obtenida 
# a partir de la razón entre valor y m^2, dividiendo el valor de venta de cada inmueble por su respectiva superficie o área. Para obtener el valor del m^2 de cada 
# inmueble utilizando listas sería necesario un bucle "for" para realizar esa operación de división en cada ítem de las dos listas y almacenar el resultado en una nueva

# ejemplo:
valor_m2 = []
for valor, m2 in zip(valor, m2):
    valor_m2.append(valor/m2)
valor_m2
# print(valor_m2) -> comentado solo para no repetir el valor en consola luego

#   Ahora crearemos dos arrays numpy para sustituir las listas creadas anteriormente

valor2=np.array([450000, 1500000, 280000, 650000, 325000])
m22=np.array([90, 150, 70, 100, 65])

#   Este procedimiento de calculo del valor del metro cuadrado utilizando arrays NumPy puede ser realizado con apenas una línea de código
valor2_m2=valor2/m22

print(valor2_m2)

# Esto muestra que la operación aritmética entre los arrays valor y m2 fue aplicada en todos los elementos sin utilizar ningún bucle for.

# ---------- Arrays de dos dimensiones ---------- 

# Considere ahora que tenemos informaciones sobre el valor de venta de cada inmueble, el valor de locación de cada inmueble, las tasas 
# incidentes sobre la venta y las tasas incidentes sobre la locación.
#   Todas estas informaciones organizadas en arrays NumPy conforme el códifo de abajo:

venta = np.array([450000, 1500000, 280000, 650000, 325000])
alquiler = np.array([1500, 2000, 1800, 2500, 1250])
tasa_venta = np.array([13500, 51000, 11200, 22750, 12350])
tasa_alquiler = np.array([900, 1000, 1100, 850, 950])

# Supongamos también que las informaciones de valores y tasas sean agrupadas en dos arrays bidimensionales(valores y tasas).

valores= np.array([venta, alquiler])
print(valores)

tasas = np.array([tasa_venta, tasa_alquiler])
print(tasas)

#   El objetivo aquí es obtener un nuevo array,"total", con el resultado de las sumas entre los valores y sus respectivas tasas,
# o sea, el nuevo array tendra dos líneas, la primera línea debe contener el resultado de la suma entre el valor de venta y tasas
# incidentes sobre la venta y la segunda línea el valor de locación más las tasas incidentes sobre la locación

total= valores+tasas
print(total)

#   Hay que notar que funciona de la misma forma con arrays de dos dimensiones. El primer elemento del array "valores" es sumado 
# con el primer elemento del array "tasas" y el resultado de esa suma es colocado en el primer elemento del array "total". Esto se
# repite para todos los elementos de los arrays involucrados.

# ---------- Operaciones aritméticas entre arrays de dimensiones diferentes - Broadcasting  ---------- 

# Este termino se utiliza para describir como NumPy trata arrays con shapes(Dimensiones) diferentes durante operaciones aritméticas. Es 
# un recurso útil que permite, con algunas restricciones, que un array menor sea "transmitido" por el array mayor para que tengan 
# dimensiones compatibles y así posibilitando las operaciones aritméticas entre ellos.

#   Puede ser algo confuso en algunos casos. Pero no profundizaremos mucho en ello por lo que los ejemplos seran simples. Como la realización 
# de una operación aritmética entre un array y una constante que es la forma más simple y utilizada de broadcasting.

#   Ejemplo:
numeros= np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

#   Considerando este array supongamos que debemos sumar el "2" en todos los elementos. Utilizando listas tendríamos que recorrer la lista con 
# un bucle for e ir iterando la suma de la constante item a item. Sin embargo con numpy se peude hacer lo siguiente:

numeros= numeros+2
print(numeros)

#   En este caso lo que hicimos es la transmisión de la constante 2 para todos los elementos del array "numeros" en la operación de suma.
#   Ahora veamos un ejemplo donde haremos una operación aritmética entre dos arrays de diferentes dimensiones. Para esto considere el siguiente array

numeros2= np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
#   Una operación bastante útil y que hace parte del calculo de estadísticas descriptivas es el cálculo de los desvíos en relación a la media.
# Para realizar este ejercicio vamos a asumir que el ultimo array tiene dos conjuntos de datos distintos y representados pro las columnas del array,
# Es decir que serian: 1, 3 y 5 y por el otro lado el conjunto compuesto por 2, 4 y 6. Vamos a considerar el array "medias" que contiene los valores
# de las medias aritméticas de cada conjunto de datos.

medias= np.array([3, 4])

#   Para obtener los descíos en relación a la media es necesario substraer cada elemento de una variable por la media de esta variable.
# por dar un ejemplo
"Las medias serian 3 y 4"
"1 - 3 | 2 - 4"
"3 - 3 | 4 - 4"
"5 - 4 | 6 - 4"

#   El broadcasting con arrays de dimensiones diferentes nos permite realizar esas operaciones de forma bastante simple

desvios= numeros2 - medias
print(desvios)

#   El próximo ejemplo es similar al anterior solo que ahroa vamos a tener el array con el shape diferente. Nuevamente tendremos dos conjuntos de datos 
# solo que ahroa ellos están representados por las dos líneas del array, es decir, el primer conjunto con valores 1, 3, 5 y el segundo 2, 4, 6

numeros3= np.array([
    [1, 3, 5],
    [2, 4, 6]
])

# Y utilizaremos el mismo array de medias.

#   Al ejecutar la operación aritmética entre el nuevo array numeros3 y el array medias vamos a tener un ValueError. Esto nos informa que no fue posible
# realizar el broadcast con dichos arrays. Lo mismo ocurre porque no respetamos las reglas del broadcasting, las que serian:

#   Para verificar si dos arrays son comparibles para una operación de broadcasting, NumPy compara sus dimensionses(shapes). La comparación comienza con las
# dimensiones finales. Dos dimensiones son compatibles para broadcasting cuando ellas son iguales o una de ellas es igual a 1 o ausente. El broadcasting será
# realizado en la dimensión ausente o de tamaño 1

#   Veamos unos ejemplos. En ellos un array de shape (2, ) será representado en la ilustración por el shape (0,2) indicando qeu el eje de las líneas está ausente
# en este array. El eje 0 es el ejede las líneas y el eje 1 es el de las columnas:

"A(3, 2)     B(0, 2)"
#   En este caso es compatible para el eje 0
"A(2, 3)     B(0, 2)"
#  No es compatible ya que falta un eje en donde esta el 2
"A(2, 3)     B(2, 1)"
#   Es compatible en el eje 1, es decir la cantidad de líneas.

#   Según las reglas de broadcasting necesitaremos modificar el shape de nuestro array de medias para hacer los arrays numeros y medias compatibles. El siguiente código
# genera un nuevo array medias con dimensiones (2, 1)

medias2=np.array([[3], [4]])
print(medias2)
print( numeros3.shape, medias2.shape)

#   Ahora tendremos una igualdad en las dimensiones del eje 0 de ambos arrays y una dimension 1 en el eje 1 del array medias. Esto indica compatibilidad para el broadcasting
# que será efectuado en el eje 1(es decir se repetira hasta tener 3 columnas como el otro array)

desvios2= numeros3 - medias2
print(desvios2)


# ------------------- Para saber más... -------------------

# numpy.nan_to_num
#   Este procedimiento sustituye valores NaN por cero o por el valor definido por el usuario en el argumento nan. Considere el siguiente array:

ejemplo=np.array([1, 2, 3, np.nan, 5])
print(ejemplo)

#   Como sabemos esto nos dice que nan es un flotante para "Not a Number". Para sustituirlo haremos lo siguiente:

np.nan_to_num(ejemplo, nan=9, copy= False)
#   Este metodo no modifica el array in-place, por ello se define "copy" y se le da el atributo False. Ademas el valor por defalto del metodo es 0, pero mencionando "nan" se puede dar otro valor

print(ejemplo)