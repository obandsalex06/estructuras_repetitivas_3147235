#ejercicio 1
# imprimir la tabla de multiplicar que el usuario 
#ingrese por teclado, utilizando el ciclo while

numero = int(input("Ingrese el numero: "))
i=10
while i <= 10:
    print(numero, "X", i, " = ", numero * i) 
    ##instruccion de incremento
    i = i - 1
    