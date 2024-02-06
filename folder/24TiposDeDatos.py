import numpy as np
#   NumPy posee algunos tipos de datos extras cuando comparamos con los tipos básicos del lenguaje python (ster, int, float y bool). La siguiente
# la siguiente tabla tiene los códigos y una descipción simple de cada tip ode dato en Numpy. Tener en cuenta que no se aborda el tipo "complex"

#   Tipo    |   Código      |       Descripción
#   int8    |   i1          |   Enteros de 8 bits con signo
#   int16   |   i2          |   Enteros de 16 bits con signo
#   int32   |   i4          |   Enteros de 32 bits con signo
#   uint8   |   u1          |   Enteros de 8 bits sin signo
#   uint16  |   u2          |   Enteros de 16 bits sin signo
#   uint32  |   u4          |   Enteros de 32 bits sin signo
#   uint64  |   u8          |   Enteros de 64 bits sin signo
#   float16 |   f2          |   Punto flotante de media precisión
#   float32 |   f4 o f      |   Punto flotante
#   float64 |   f8 o d      |   Punto flotante de doble precisión(compatible con el objeto float de python)
#  float128 |   f16 o g     |   Punto flotante de precisión extendida
#   bool    |   ?           |   Tipo booleano
#   object  |   El          |   Tipo objeto de Python
#   string  |   S           |   Tipo string
#   unicode |   U           |   Tipo Unicode    

#   Podemos hacer alguns observaciones sobre las informaciones de la tabla de arriba. En los enteros tenemos dos tipos, int y uint. Los int consideran los signos de los números, mientras que los
# uint(unsigned integer) no los considera. Es decir no representa negativos. Para dar un ejemplo usaremos los enteros de 8 bits que pueden codificar 256 números (n bits disponibles pueden codificar 2^n números).
# Con esto deducimos que los enteros de 8bits(int8) representan los números de -128 hasta 127 y los enteros sin signo de 8 bits(uint8) representan los números de 0 hasta 255.

#   Para los números de punto flotante tenemos cuatro tipos de precisión diferentes, siendo que el float64 es el tipo compatible con el float de Python.

#   Los últimos tipos, string y unicode tienen tamaños fijos y para que creemos un dtype con tamaño 15, por ej, debemos utilizar "S15" como codigo para string y "U15" para unicode.

'Ejemplo'
array= np.array(['AB', 'CD'], dtype='U2')
print(array, array.dtype, array.shape)