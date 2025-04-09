#Es una estructuctura o una coleccion de datos 
#que los almacena en pares de clave-valor
# - Un diccionario comienza y termina
# con llaves (curly braces){}
# - la clave se separa del valor por dos puntos (:)
# - cada elemento (Propiedad) del diccionario se separa por comas (,)
# - cada clave es un string (cadena)
# - el valor puede ser de cualquier tipo de dato

# [] = listas
# {} = diccionarios
#ejemplo: Diccionario
#que almacene los datos de un pais
pais1 = {
            "nombre": "Argentina",
            "capital": "Buenos Aires",
            "moneda": "Peso argentino",
            "ciudades": [
                "Córdoba",
                "Rosario",
                "Mendoza"
                        ],
            "poblacion":{
                        "censo": 46,
                        "densidad": 16
                        }
        
        } 
  
pais2 = {
            "nombre": "Ecuador",
            "capital": "Quito",
            "moneda": "Dolar",
            "ciudades": [
                "Guayaquil",
                "Cuenca",
                "Loja"
                        ],
            "poblacion":{
                        "censo": 17,
                        "densidad": 12
                        }
        
        }

pais3 = {
            "nombre": "Paraguay",
            "capital": "Asunción",
            "moneda": "Guaraní",
            "ciudades": [
                "Ciudad del Este",
                "Encarnación",
                "Asunción"
                        ],
            "poblacion":{
                        "censo": 7,
                        "densidad": 5
                        }
        }    
            
#Acceder a la informacion del pais
print(pais1["moneda"])
print(pais1["capital"])
#Acceder a una ciudad del pais 1
print(pais1["ciudades"][1])
print("--------------")
#Iterar las ciudades del pais 1
for ciudad in pais1["ciudades"]:
    print(ciudad)
    
#Acceder a datos poblacionales
print("--------------")
print("censo:", pais1["poblacion"]["censo"], "millones de habitantes")
print("densidad:", pais1["poblacion"]["densidad"], "hab/km2")
