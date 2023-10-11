
#los inputs son neuronas que estamos codeando basicamente, los valores que van a tener digamos
#cada input va a tener un valor asociado a el input anterior, es decir la misma cantidad es lo que necesitamos de "pesos" o weights
#cada neurona unica va a tener una "bias" unica

inputs = [1, 2, 3] 
#inputs son dos cosas: un vector de valores, como se ve antes.
#  O bien  son valores de nuestras neuronas previas O BIEN son datos que fueron entregados a nosotros.
#  Esto nos permitira encontrar errores o sucesos.
#al ser 3 inputs solamente, seran los extremos de la neurona, si tenemos 4 sera de la capa del medio

weights = [0.2, 0.8, -0.5]
#

bias=2
#esto es bias:
#El bias o sesgo puede ser pensado como un modelo que no ha tenido en cuenta toda la información disponible en el dataset, 
# y, por lo tanto, es demasiado pobre como para hacer predicciones precisas. Esto se conoce como underfitting 
# y ocurre cuando el modelo es demasiado simple para el problema que se quiere solucionar

#lo primero que necesitamos es sumar los inputs multiplacados por los weights.
##Lo siguiente es el output de nuestra red neuronal
#basicamente necesitamos saber que son las listas o arrays. Esto es lo basico de las redes neuronales.
output= inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2] + bias
print(output)
#el comando anterior hara que aparezca el valor en consola.
#cada "neurona" tiene solo una "bias", pero cada valor de los inputs tiene su propio peso.
#para poder obtener el valro que queremos debemos saber como modificar los weights y
#bias para que el output sea los valores que nosotros queremos.