# Instruccion "for" anidada

# Es una forma de crear un bucle o loop dentro de otro. Bastante útil para iterar en estructuras de datos mas complejas como secuencias y diccionarios anidados.

# Debajo tenemos un formato patrón apenas para enseñar que los loops mas internos deben estar siemrpe identados. Eso hara que Python entienda que se trata de un bucle for dentro de otro.

#Formato patrón

# for <item_1> in <iterável_1>:
#     for <item_2> in <iterável_2>:
#         <intrucciones>

# Tomemos por ejemplo la lista anidada datos con el conjunto de accesorios de tres vehículos. El objetivo es transformar esta lista anidada en una lista simple con todos los
# accesorios de los tres vehiculos.
datos	=	[	
				['Llantas	de	aleación',	'Cerraduras	eléctricas',	'Piloto	automático',	'Bancos	de	cuero',	'Aire	acondicionado',	'Sensor	de	estacionamiento',	'Sensor	crepuscular',	'Sensor	de	lluvia'],
				['Central	multimedia',	'Techo	panorámico',	'Frenos	ABS',	'4	X	4',	'Panel	digital',	'Piloto	automático',	'Bancos	de	cuero',	'Cámara	de	estacionamiento'],
				['Piloto	automático',	'Control	de	estabilidad',	'Sensor	crepuscular',	'Frenos	ABS',	'Cambio	automático',	'Bancos	de	cuero',	'Central	multimedia',	'Vidrios	elétricos']
            ]

# Haciendo un loop simple tenemos acceso a las tres listas individualmente.

# for lista in datos:
#     print(lista)

# De la siguiente forma accedemos a los items de cada lista en un mismo procedimiento de iteración, utilizando un nuevo bucle for anexado al anterior, teniendo como iterable la lista proveniente del
# anterior.

# for lista in datos:
#     for item in lista:
#         print(item)

# Para crear una nueva lista con todos los accesorios del dataset basta ejecutar el código abajo.
accesorios=[]
for lista in datos:
    for item in lista:
        accesorios.append(item)

print(accesorios)