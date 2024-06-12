
#condicional IF
"""
color =input("Adivina cual es el color: ")

if color == "Rojo":
    print ("Muy bien, ese es el color")
else:
    print("Ese no es el color")
"""
# Operadores de comparacion.
# ( == : Igual ) ( != : Diferente) ( < : Menor que ) (> : Mayor que ) (>= mayor o igual que )
# ( <= : Menor o igual que) 
"""
year = int(input("Ingrese un año: "))


if year==2001:
    print("Este es el año")
else:
    print("Ese no es el año")
"""
# Vamos a ver una nueva forma de validar una condicion (elif)  

# Operadores logicos  
# (and : Y) (or : O) (! : Negacion ) (not : No)

"""
dia = int(input("Ingrese el dia"))
if dia==1:
    print("Lunes")
elif dia==2:
    print("Martes")
elif dia==3:
    print("Miercoles")
elif dia==4:
    print("Jueves")
else:
    print("Otro dia")
"""

# Vamos a realizar algunas pruebas 

pais = input("Ingrse el pais")

if pais == "Colombia" or pais =="Peru" or pais=="Chile":
    print(f"el {pais} Hablan Español")
else:

    print("No hablan Español")


