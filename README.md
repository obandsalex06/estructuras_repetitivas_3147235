# estructuras_repetitivas_3147235
proyecto para trabajar ciclos for y while en python

##Conceptos clave para trabajar en ciclos:
* **Breakpoint (Punto de interrupcion)**: para ejecutar codigo, una instruccion a la vez (depuracion - debugger).
Permite ver el valor de las variables definidas en un programa a traves de la ejecucion de codigo, permitiendo observar el comportamiento del programa/codigo a traves del tiempo

* **variable contadora (contador)**: Variable a la cual podemos aumentar o disminuir su valor en una determinada cantidad constante (de uno en uno, de dos en dos, etc).
- **iteracion**: es un recorrido en la ejecucion de un ciclo.

**Instruccion de incremento**
(sintaxis):

1. i = variable contadora
2. = = operador de asignacion
3. i = variable contadora
4. +/- = operador, incremento (+), decremento(-)
5. 1 = valor en que se aumenta la variable.

- una variable contadora se debe inicializar **obligatorio** antes del ciclo/estructura repetitiva, con un valor inicial(0)
- Una variable contadora, por lo general se nombra con las letras i,j.
- una variable contadora **debe participar en la condiconal del ciclo** 
## ciclo while.
-Toda variable contadora debe tener una **isntruccion de incremento** para aumentar su valor 

estructura que permite ejecutar un bloque de codigo de numero determinado de veces.
El bloque de codigo dentro del ciclo while se ejecutara sucesivamente 
**mientras la condicional sea evaluada como verdedera.**

### sintaxis en python

```
while condicional:
    instruccion1
    instruccion2
    instruccion3
    .....
    instruccion n
```

## ciclo for se utiliza (python) para recorrer 
conjuntos de datos (estructuras de datos - colecciones de datos)
# el ciclo recorrera cada dato en la estructura desde el primero hasta el ultimo

**el recorrido se asigna a una variable en el ciclo**

### sintaxis for :
```
for <variable> in <conjunto de datos>:
      instruccion1
       
```