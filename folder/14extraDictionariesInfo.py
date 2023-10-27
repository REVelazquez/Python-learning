# Para saber mas:
# deepcopy()
# El tproblema se da a la hora de trabajar con objetos compuestos(anidados) como es el caso del diccionario dataset
# que se encuentra en el codigo debajo. Este es un diccionario que tiene como valores otros diccionarios
# que a su vez tienen como valores listas.

dataset={
    'Dodge':{
        'motor': 'Motor 6.7',
        'año': 2017,
        'km': 45757,
        'accesorios':['Llantas de alineación', '4 x 4', 'Central multimedia'],
        'valor':92615.1
    },
    'Ford':{
        'motor': 'Motor 2.4 Turbo',
        'Cero_km': True,
        'km': 80000,
        'accesorios': ['Control de tracción', 'Bancos de cuero', 'Control de estabilidad'],
        'valor':51606.59
    }
}

# Ahora relizaremos una copia para agregar un valor a nuestro dataset

datos=dataset.copy()

# datos['Dodge']['accesorios'].append('Airbag') <-- esta comentado para que no afecte a lo que sigue
# print(datos)

# Si bien es agregado a la copia, en el caso de agregar un print para dataset veremos que en el diccionario
# original tambien se agrego el valor "Airbag". Esto sucede porque "copy" crea una referencia al diccionario
# es decir, se crea una copia superficial del mismo, por lo que esta copia alcanza los objetos mutables
# dentro del objeto copiado.
# Para solucionarlo podemos utilizar la biblioteca "copy" de python que pone a disposicion metodos de copia 
# superficial y profunda. La diferencia entre uno y otra es la relevancia para objetos compuestos.

# Como dijimos antes, una copia superficial solo hace referencia al objeto original. En una copia profunda se
# construye un nuevo objeto anidado y entonces, recursivamente, son insertados en copias de los objetos en el original.

# Para utilizar los metodos de dicha biblioteca necesitamos importar el paquete para nustro proyecto. Para eso utilizamos
# import seguido del nombre de la biblioteca que deseamos cargar en el proyecto.

import copy

# Ahora usaremos el metodo deepcopy() como en el siguiente ejemplo:

dataset_copia= copy.deepcopy(dataset)

# con esto podemos hacer cambios en la copia de nuestro primer dataset y no se veran reflejados en el original:

dataset_copia['Dodge']['accesorios'].append('Bancos de cuero')

print(dataset_copia, ' y aqui esta el original', dataset)
# en el print anterior se puede sacar el string y "dataset" si se quiere que la consola muestre menos info