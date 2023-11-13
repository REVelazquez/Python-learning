# Las funciones son unidades de código reutilizables que realizan una tarea específica, pueden 
# recibir alguna entrada y también retornar algún resultado. Utilizar funciones ayuda en la 
# organización y reutilización del código haciendo que el programa tenga un número menor de líneas
# de codigo y por lo tanto sea de fácil lectura y depuración.

# Python al igual que otros lenguajes, cuenta con funciones precargadas, llamadas built-in. A su vez
# nosotros podemos crear propias como se vera mas adelante.

# Buit-in Functions.

# Algunas de estas ya se vieron previamente, como type(), print(), zip, entre otras. 
# La tabla de debajo presentara las funciones built-in de python.

#                                Built-in Functions
# abs()         |   dict()      |   help()          |   min()       |   setattr()
# all()         |   dir()       |   hex()           |   next()      |   slice()
# any()         |   divmod()    |   id()            |   object()    |   sorted()
# ascii()       |   enumerate() |   input()         |   oct()       |   staticmethod()
# bin()         |   eval()      |   int()           |   open()      |   str()
# bool()        |   exec()      |   isinstance()    |   ord()       |   sum()
# bytearray()   |   filter()    |   issubclass()    |   pow()       |   super()
# bytes()       |   gloat()     |   iter()          |   print()     |   tuple()
# callable()    |   format()    |   len()           |   property()  |   type()
# chr()         |   frozenset() |   list()          |   range()     |   vars()
# classmethod() |   getattr()   |   locals()        |   repr()      |   zip()
# compile()     |   globals()   |   map()           |   reversed()  |   __import__()
# complex()     |   hasattr()   |   max()           |   round()
# delattr()     |   hash()      |   memorybied()    |   set()

# En algunos casos utilizar una de ellas nos permite reducir código y hasta generar una mejora en el 
# performance. Por ejemplo, tenemos el diccionario:

datos = {'Jetta Variant':88078.64, 'Passat':106161.94, 'Crossfox': 72832.16}

# si quisieramos obtener una lista simple con solo los valores, deberiamos hacer un loop, lo que serian tres lineas de código,
# sin embargo podemos utilizar la funcion list y tendremos una lista de la misma forma que haciendo esas lineas:

valores= list(datos.values())
print(valores)

# Si queremos hacer una suma de dichos valores podriamos utilizar la funcion sum() de la siguiente forma:

total= sum(datos.values())
print('El valor total es', total)

# Con esto ya podemos notar las cualidades de las build-in functions, es decir, simplificar un codigo para que ocupe menos lineas
# Se puede encontrar una mejor explicacion en la documentacion relativa de python. A la vez podemos acceder a esta misma en nuestra pc
# si utilizamos la funcion help(). Para ello debemos llamarla y pasar como argumento el nombre del recurso del cual queremos obtener infor-
# -mación de ayuda. Por ejemplo: help(print) que nos devolvera que es lo que hace "print()". Otra forma es utilizar un "?" antes o luego
# del recurso del cual queremos obtener información.

