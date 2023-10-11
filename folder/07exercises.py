carro_1	=	['Dodge	Jorney',	'Motor	3.0	32v',	2010,	99197,	False,	['Vidrios	eléctricos',	'Piloto	automático',	'Techo		panorámico',	'Aire	acondicionado'],	120716.27]
carro_2	=	['Carens',	'Motor	5.0	V8	Bi-Turbo',	2011,	37978,	False,	['Aire	acondicionado',	'Panel	digital',	'Central	multimedia',	'Cambio	automático'],	76566.49]
carro_3	=	['Ford	Edge',	'Motor	Diesel	V6',	2002,	12859,	False,	['Sensor	crepuscular',	'Llantas	de	aleación',	'Techo	panorámico',	'Sensor	de	lluvia'],	71647.59]
# 1. Crear una secuencia con nombre "carros" que contenga las informaciones de los 3 veihiculos.

carros= carro_1, carro_2, carro_3

# 2.	 Utilizando	 una	 de	 las	 operaciones	 con	 secuencias	 que	 aprendimos,	 verifique	 en	 la	 secuencia carros		si	el	vehículo	Ford	Edge	tiene	como	accesorio Sensor	de	lluvia
'Sensor	de	lluvia' in carros[2][5]
#otra opcion seria carros[-1][-2]

# 3. Obtenga los códifos qeu tienen como resultado el siguiente conjunto de selecciones en la secuencia "carros"
# a) 2002
# b) ['Vidrios	eléctricos',	'Piloto	automático',	'Techo		panorámico',	'Aire	acondicionado']
# c) 'Cambio automatico'
# d) ['Panel digital', 'Central	multimedia']

# a)
carros[2][2]

# b)
carros[0][5]

# c)
carros[1][5][-1]

# d)
carros[1][5][1:3]

# 4. Obtenga la sumatoria de los valores de mercado de los tres vehículos de la secuencia carros.

valores= carros[0][-1]+ carros[1][-1]+ carros[2][-1]

print(valores)