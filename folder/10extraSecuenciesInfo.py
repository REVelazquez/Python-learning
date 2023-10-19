# Desempaquetado de tuplas 
# En python podemos asignar variables distintas a cada elemento de una tupla utilizando
# un recurso bastante simple, veamos un ejemplo:

ejemplo1= 22, 30, 5

# Ahora para colocar cada uno en una variable debemos hacer lo siguiente:

posicion1, posicion2, posicion3 = ejemplo1

print(posicion1, ' Aca inicia el valor 2: ', posicion2, ' Aca inicia el valor 3: ', posicion3)

# zip()
# Esta fincon retorna un iterador de duplas, donde la i-ésima tupla contiene el i-ésimo
# elemento de cada una de las secuencias de argumentos o iterables.
# por ejemplo:

carros= ['C4', 'Fit', 'Focus']
fabricantes= ['Citroën', 'Honda', 'Ford']

# cuando pasamos estas variables como argumento para la funcion zip() creamos un iterador 
# que agrega los elementos de cada una de las listas.
zip(carros, fabricantes)

#la salida sera:
print(list(zip(carros, fabricantes)))

# set()
# Python tambien permite la creacion de conjuntos con el uso de esta funcion. Los conjuntos son
# colecciones de elementos únicos y no ordenados. veamos el siguiente codigo donde
# se crea una tupla para darnos un ejemplo de esto.

ejemplo3 = 'C4', 'Fit', 'Focus', 'Gol', 'Focus', 'C4', 'Up!'

# Existen dos formas de crear un conjunto. La primera es con el uso de la funcion set() y el segundo es
# utilizando llaves {}
# Un uso bastante comun de los conjuntos es para la eliminacion de valores duplicados.
# Esto es lo que ocurre cuando usamos la tupla anterior para crear un conjunto

print('Tupla original: ', ejemplo3, ' una vez que utilizamos set():', set(ejemplo3))

# como se menciono antes, aqui podemos ver como se borran los valores repetidos.