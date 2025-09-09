print("Hola Mundo")

# Variables y tipos de Datos
nombre = "Ever"
edad = 25
altura = 1,60
es_estudiante = True
print ("Nombre:",nombre)
print ("Edad:",edad)
print("Altura:",altura)
print("¿Es estudiante?",es_estudiante)


#Programa
nombre = input("¿Cual es tu nombre?")
edad = int(input("¿Cuantos años tienes?"))
print(f"Hola{nombre}, tienes{edad}años")

import datetime
año_actual = datetime.datetime.now().year
año_cumple_100 = año_actual + (100 - edad)
print(f"Cumpliras 100 años en el año{año_cumple_100}")

import datetime
año_actual = datetime.datetime.now().year
año_cumple_100 = año_actual + (100-edad)

