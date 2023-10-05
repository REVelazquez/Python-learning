#suma

sum = 2+2
print('suma :'+ str(sum))

#resta

diferencia = 4-2 
print('resta: '+ str(diferencia))

#multiplicacion

producto = 4*3
print('producto: '+ str(producto))

#division (/) y (//)

# la division / devuelve un flotante.
fraccion= 13/3
print('division /: '+ str(fraccion))

# la division // devuelve un entero resultado de la division de dos numeros
fraccion2= 13//3
print('division //: '+ str(fraccion2))

#potencia (**)

elevacion= 9**3
print( 'potencia: '+ str(elevacion))

#resto de division (%)
resto = 13%3
print('resto: '+ str(resto))

#expresiones matematicas: hay que tener cuidado cuando se hacen operaciones complejas ya que siguen el mismo reglamento que matematica

operacion1= 4*3**2-5*2
#la potencia tiene la mayor prioridad

operacion2= 4*3**(2-5)*2
#en este caso los parentesis tienen mas prioridad que la potencia

operacion3= (4*3)**2-5*2
#nuevamente los parentesis tienen mas prioridad, luego viene potencia, multiplicacion/division, suma y resta

print(
    'resultado 1: ' + str(operacion1) +
    ', resultado 2: '+ str(operacion2)+ 
    ', resultado 3: '+str(operacion3)
)
