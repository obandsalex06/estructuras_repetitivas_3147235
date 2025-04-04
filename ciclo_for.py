#ciclo for 
#especial para recorrer 
#estructuras de datos
#todo lo que esta entre
#[] se denomina lista

#funcion range(Python)
#Crea una lista de numeros en el rango definido
#por el usuario
 
 
numero = int(input("Ingrese un numero: "))

for i in range(1, 11):
    resultado = numero * i 
    print(numero, "X", i, "=", resultado)