# Variables para los ejercicios
carro_1	=	['Dodge	Jorney',	'Motor	3.0	32v',	2010,	99197,	False,	['Vidrios	eléctricos',	'Piloto	automático',	'Techo	panorámico',	'Aire	acondicionado'],	120716.27]
carro_2	=	['Carens',	'Motor	5.0	V8	Bi-Turbo',	2011,	37978,	False,	['Aire	acondicionado',	'Panel	digital',	'Central	multimedia',	'Cambio	automático'],	76566.49]
carro_3	=	['Ford	Edge',	'Motor	Diesel	V6',	2002,	12859,	False,	['Sensor	crepuscular',	'Llantas	de	aleación',	'Techo	panorámico',	'Sensor de lluvia'],	71647.59]

# 1. Seleccione la lista de accesorios de cada vehiculo y cree una nueva lista con la concatenacion de los accesorios de los tres vehiculos llame a esa lista accesorios

accesorios= carro_1[5] + carro_2[-2] + carro_3[-2]

# 2. Coloque los items de la lista creada arriba en orden alfabética.

accesorios.sort()

# 3. Note que los items 'Aire acondicionado' y 'Techo paronamico' estan duplicados en nuestra lista de accesprops. Elimine el ítem 'Aire acondicionado' con el uso del método remove
accesorios.remove('Aire	acondicionado')

# 4. Elimine el ítem 'Techo panorámico' con el uso del método pop

accesorios.pop(-2)

# 5. Agrega el item 'Bancos de cuero' en la segunda posicion

accesorios.insert(1, 'Bancos de cuero')

# 6. Agrega al final de la lista "Camara de estacionamiento"

accesorios.append('Camara de estacionamiento')