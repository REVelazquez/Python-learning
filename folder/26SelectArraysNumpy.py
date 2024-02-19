import numpy as np
#   Debemos hablar sobre indexación y selección con arrays NumPy. A esto l otratamos cuando trabajamos con secuencias que tienen bastante similaridad con arrays NumPy.

#   Para facilitar nustro entendimiento vamos a utilizar un array bidimensional conteniendo strings que representan letras y números.

letras= np.array(['A', 'B', 'C', 'D', 'E'])
numeros= np.arange(1, 6)
datos = np.array([letras, numeros])

print (datos, datos.dtype)

# ------------------- Indexación -------------------

#   Así como en las secuencias integradas de Python, la indexacion en arrays NumPy tiene origen en el cero.
#   En un array unidimensional el proceso de selección de ítems es bastante simple, bastando indicar el indice del elemento que se quiere seleccionar entre corchetes luego
# del nombre del array. El siguiente ejemplo muestra como seleccionar el primer elemento del array letras

print(letras[0])
#   El uso de índices negativos también es permitido en las selecciones con arrays NumPy. Recordando que para seleccionar el último elemento de un array utilizamos el índice -1,
# para selecionar el penúltimo elemento utilizamos el índice -2 y así sucesivamente. Abajo veremos un ejemplo de selección del último elemento del array letras.

print(letras[-1])

#   Para selecciones en arrays bidimensionales necesitamos realizar un paso extra. Esto es porque cuando estamos utilizando un único índice estamos accediendo a las informaciones
# del eje 0, es decir, accediendo a arrays unidimensionales.

print (datos[0])
print(datos[1])

#   Para acceder a un ítem específico dentro de un array bidimensional podemos proceder de dos formas:

print(datos[1][2])

datos[1, 2] # Al hacer esto es como si hiciera lo anterior

#   En este tipo de indexación, primero pasamos el índice del eje 0(líneas) y después el índice del eje 1(columnas)

"Por ello la selección en arrays bidimensionales es: array[línea][columna] o bien: array[línea, columna]"

# ------------------- Slices  -------------------

#   En ellos seleccionamos trechos de arrays con el uso de índices. La sintaxis para realizarlos, en un array NumPy unidimensional es array[i : j: k] donde i es el índice inicial,
# j es el índice de parada y k es el indicador de paso (K !== 0). Importante también saber qeu en los slices el ítem con índice i es incluido y el ítem con índice j no es incluido
# en el resultado.

#   Vamos a verificar algunos ejemplos de slices con arrays unidimensionales. El código de abajo selecciona los elementos de índice 1, 2 y 3 del array letras. El elemento del índice
# inicial en el resultado de los slices y el elemento del índice inicial en el resultado de los slices y el elemento del índice de parada no entra en resultado. Ej:

print(letras[1:4])

#   En el caso que queramos incluir el primer elemento del array hasta cierto punto de parada j, basta suprimir el primer índice en el slice. El mismo tendria el siguiente código: 
# array[:j]
print(letras[:4])

#   En cambio si suprimimos ambos nos dara el array completo
print(letras[:])

#   Ahora imagina que necesitamso hacer una selección de elementos que no están puestos de forma continua en un array. Supongamos que necesitamos seleccionar los valores pares o 
# impares de una secuencia de números. Para eso utilizamos, en la notación patrón, el indicado de paso, el cual nos informa cuantas posiciones debemos saltar entre una seleccion y otra
# Observa el siguiente ejemplo:

print(numeros[::2])

#   A tener en cuenta que como queremos solo los impares no es necesario informar el índice de partida ni el de parada, también podriamos haber usado [0:5:2] para tener el mismo resultado
#   Para seleccionar solamente los números pares del array el código sera:

print(numeros[1::2])

#   En estos casos hacemos una seleccion de intervalos de tamaño 2, teniendo como única diferencia el punto de partida.
#   La idea es la misma en arrays bidimensionales, salvo algunas pequeñas diferencias por estar trabajando con dos ejes. Ejemplo:

print(datos[:, 1:3])

#   Aqui hay que tener en cuetna que las notaciones array[línea][columna] y array[línea, columna] no son equivalentes cuando hacemos slice en un array vidimensional. Solo son equivalentes en la
# selección de valores únicos en un array bidimensional.

#   Si en estos arrays utilizamos la notación array[i : j : k, x : y : z] donde i y x son los índices iniciales, j y y son los índices de parada,mientras k y z son los indicadores de paso(k y z !== 0)
# para los ejes 0 y 1 respectivamente.

#   En el ejemplo anterior estamos informando que queremos en nuestra selección todos los elementos del eje 0([:]) y apenas los elementos con índices 1 y 2 del eje 1([1:3])
#   Volviendo al ejemplo de los númeors pares, vamos a aplicar slice al array datos para obtener una visualización de los elementos que están en las columnas con números pares.

print(datos[:, 1::2])
#   La misma idea del ejemplo unidimensional solo que aquí fue necesario informar que queríamos todos los elementos del eje 0(líneas) en nuestra visualización

# ------------------- Indexación con array booleano -------------------

#   Del mismo modo que realizamos operaciones aritméticas entre arrays, las operaciones de compración entre ellos también son posibles. La diferencia es que en estas operaciones de comparación tendremos
# como resultado un array booleano. Por ejemplo:

contador = np.arange(5)
print(contador)
contador=contador >= 2
print(contador)

#   Aqui ocurre lo mismo que con el broadcasting. Solamente que ahora utiliamos operadores de comparación y no aritméticos.
#   Lo interesante de tener como respuesta arrays booleanos es que los podemos utilizar cuando estemos indexando otro array. Regresando al ejemplo anterior:

contador=[[contador]]
print(contador)

#   En los arrays bidimensionales funciona de la misma forma que lo anterior, pudiendo hasta mezclar arrays booleanos e índices enteros. Podemos también asignar el array booleano en una nueva variable y pasar esta variable como índice.

select = datos == 'A'
print(select)

print(datos[select])

#   Podemos utilizar operadores lógicos para hacer las selecciones más complejas. Los operadores lógicos and, or y not de Python no funcionan con arrays booleanos, para eso utilizamos &, | y ~. En este caso las expresiones antes y después
# de los operadores lógicos deben estar siempre entre paréntesis, como a continuación:

select= (datos == 'A') | (datos == 'D') | (datos == '2')
print(select) # Nos devolverá valores booleanos según se cumpla o no

print(datos[select]) # Nos devolverá valores que cumplen las condiciones

print(datos[~select]) # Nos devolverá todos los valores que no cumplan las condiciones

#   Para tener como retorno un array en el formato bidimensional necesitamos pasar las informaciones de slices por eje, como se hizo anteriormente.
#   Vamos a suponer que necesitamos seleccionar las columnas que contienen los elementos 'A', 'D', y '2'. Observemos la diferencias entre el código anterior y el de abajo:

select=(datos[0]=='A') | (datos[0] == 'D') | (datos[1] == '2')
print(select)
print(datos[:, select])
print (datos[:, ~select])

#   Notamos que el array booleano ahora es unidimensional y debe ser pasado como índice del eje 1(columnas). Y una observación importante: EL ARRAY BOOLEANO DEBE TENER EL MISMO TAMAÑO DEL EJE DEL ARRAY QUE ESTÁ SIENDO INDEXADO. En el ejemplo
# vemos un array booleano con cinco elemento yestamos indexando el eje 1 que también tiene cinco elementos

#   Otro punto a tener en cuenta es que el código de selección ahora informa el slice para el eje 0(todas las líneas) y para el eje 1(Array booleano).
#   Para finalizar esta sección vamos a crear un slice del array "datos"