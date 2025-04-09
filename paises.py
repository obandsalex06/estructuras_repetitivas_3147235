paises = [
        pais1 := {
            "nombre": "Venezuela",
            "capital": "Caracas",
            "moneda": "Bolívar",
            "poblacion": {
                "censo": 28,
                "densidad": 31
                
                         },
            "superficie": "916.445 km2",
            "ciudades": [
                    "Carabobo",
                    "Maracaibo",
                    "Barquisimeto"
                    "Valencia",
                        ]
        },
        pais2 := {
            "nombre": "Brasil",
            "capital": "Brasilia",
            "moneda": "Real",
            "poblacion": {
                "censo": 213,
                "densidad": 25
                         },
            "superficie": "851.576 km2",
            "ciudades": [
                    "São Paulo",
                    "Río de Janeiro",
                    "Salvador"
                        ]
        },
        pais3 := {
            "nombre": "Paraguay",
            "capital": "Asunción",
            "moneda": "Guaraní",
            "poblacion": {
                "censo": 7,
                "densidad": 5
                         },
            "superficie": "406.752 km2",
            "ciudades": [
                    "Ciudad del Este",
                    "Encarnación",
                        ]
        }
        ]

#recorrer todos los paises
print("Recorriendo todos los paises")

for pais in paises:
    print("Ciudades principales:")
    for ciudad in pais["ciudades"]:
        print("-", ciudad)
    print("Nombre: ", pais["nombre"])
    print("Capital: ", pais["capital"])
    print("Moneda: ", pais["moneda"])
    print("Poblacion:")
    print("censo: ", pais["poblacion"]["censo"], "millones")
    print("densidad: ", pais["poblacion"]["densidad"], "hab/km2")
    print("superficie: ", pais["superficie"])
    print("--------------------")