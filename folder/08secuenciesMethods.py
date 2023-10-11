# En la misma forma que existen operaciones existen metodos de secuencias. Los que se veran a continuacion SOLAMENTE
# son soportados por secuencias mutables.

# Operación         |       Resultado
# A.sort()          |       Ordena la lista A
# A.append(x)       |       Agrega el elemento x al final de la lista A
# A.insert(i, x)    |       Inserta x en la secuencia A en el indice informado por i
# A.remove(x)       |       Elimina la primera ocurrencia de x de la secuencia A
# A.pop([i])        |       Elimina y retorna el elemento de indice i de la secuencia A
# A.clear()         |       Elimina todos los items de la secuencia A.
# A.copy()          |       Crea una copia de la secuencia A.

#Veamos algunos ejemplos

# A.sort()
numbers= [1, 10, 5, 20, 12]
numbers.sort()
print(numbers)
# si escribimos reverse= True dentro del argumento de "sort" nos dara la lista ordenada al revez

# A.append(x)

numbers.append(25)
print(numbers)

# A.insert (i, x)

numbers.insert(2, 8)
print(numbers)

# A.remove(x)
numbers.remove(8)
print(numbers)

#A.pop[i]

numbers.pop()
print(numbers)
#si al hacer pop no indicamos que número queremos que saque, es decir su index, lo hara con el ultimo de la lista

# A.clear
numbers2= [11, 22, 55, 30]
numbers2.clear()
print(numbers2)

# A.copy
numbersCopy=numbers.copy()

numbers.append(30)
print(numbersCopy, ' es diferente al original modificado: ', numbers)