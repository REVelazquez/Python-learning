# Existen dos tipos Mutables e inmutables. EN las mutables tenemos las listas, tambien conocidas como arrays.
# Las inmutables son tuplas y range

#listas: son basicamente arrays, es decir se enseñan de la forma [], teniendo valores dentro de los corchetes
#a su vez los indices de las posiciones de los elementos van de "0" hasta la cantidad de valores menos uno, es decir:
# 'n-1' valores. Hay diferentes formas de crear una lista, por ejemplo:
# utilizando un par de corchetes y separando elementos con comas: [1, 2, 3, 4]
# utilizando dos corchetes: [], [1]
# utilizando list() o list(iterator)
# veamos algunos ejemplos:

# este es el primer caso de listas
accesorios = ['Llantas_de_aleación',	'Cerraduras_eléctricas',	'Piloto_automático',	'Bancos_de_cuero',	
'Aire_acondicionado']

print(type(accesorios), accesorios)

# este es el segundo caso de listas
accesorios2 = ['Llantas_de_aleación',	'Cerraduras'],	['Piloto_automático',	'Bancos_de_cuero',	
'Aire_acondicionado']

print(type(accesorios), accesorios)

# este es el tercer caso de listas
newList = list('12345')

print(type(newList), newList)
# hay que recordar que en las listas pueden existir diferentes tipos de datos, no necesariamente tienen que ser numeros o strings, tambien pueden
# ser otras listas, objetos, bolleanos, etc

#Tuplas: una diferencia con las listas es que son inmutables, ademas su delimitadores son parentesis, la indexacion de sus valores es como el 
# de las listas. Ademas pueden ser construidas de varias formas:
# Utilizando un par de parentesis: ()
# Utilizando una coma a la derecha: x,
# Utilizando un par de parentesis con items separados por una coma: (x, y, z)
# Utilizando: tuple() o tuple(iterador)
# por ejemplo:

tupla1= 1, 2, 3

print(type(tupla1), tupla1)

tupla2= ('Hola', 2023)

print(type(tupla2), tupla2)

tupla3= tuple([2, 5, "Jack"])

print(type(tupla3), tupla3)