# La mayoria de secuencias soportan las siguientes operaciones,
# Operacion             |       Resultados:
# x in A                |       Retorna True si un elemento de la secuencia A es igual a x.
# not in A              |       Retorna False si en un elemento en A es igual a x.
# A + B                 |       Concatena las secuencias A y B
# len (A)               |       Retorna el tamaño de la secuencia A.
# A[i]                  |       Retorna el i-ésimo item de la secuencia A.
# A[i:j]                |       Recorta la secuencia A del indice "i" hasta el "j". En esta secuencia el elemento con indice "i" es incluido y el elemento con indice "j" no es incluido en el resultado.
# A[i:j:k]              |       Recorta la secuencia A del indice "i" hasta el "j" con el paso "k". En esta secuencia el elemento con indice  "i" es incluido y el elemento con indice j no es incluido en el resultado.
# A.index(x)            |       Retorna el indice de la primera ocurrencia  de x en la secuencia A.
# A.count(x)            |       Retorna el total de ocurrencias de "x" en la secuencia A.

# Veamos algunos ejemplos:
# operacion "x in A"

numbers= [12, 34, 50, 1, -6]

print(50 in numbers)

# x not in A

print(50 not in numbers)

# A+B

numbers2= ['lista 2', .2, 66, .5, -8]

print(numbers+numbers2)

#esto tambien sirve con tuplas

tupNumbers = 8, 5, 21, 33

tupNumbers2= 'tupla2', 9, 5, 6, 4, 9

print(tupNumbers+ tupNumbers2)

# len(A)

print (len(numbers), len(tupNumbers+tupNumbers2))

# A.index(X)

print (tupNumbers2.index(6))

# A.count(x)

print (tupNumbers2.count(9))

# A[i] retorna elvalor del indice indicado, funciona en listas y tuplas

print(numbers[1], tupNumbers2[0])

# Esto tambien sirve para listas anidadas, por ejemplo:

anidadas= [1, 2, 3, ['holi', 4, 5, 6]]

print(anidadas[3][0])
# En este caso al ser una lista anidada tenemos que definir la posicion donde esta la lista dentro de la otra y el elemento que queremos retornar


# A[i:j]

combined = numbers+ numbers2

print(combined[1:4])
# Esta operacion tiene algunas cualidades que permiten al omiter una parte de la misma funcione de una u otra forma

print( combined[:4], combined[5:])

# A[i:j:k] esta operacion de slice funciona como la anterior con la diferencia de que avanza en pasos "k"
# permitiendo que algunos valores quedan fuera, es decir funciona como range.

print(combined[1:6:2])