#Creo el diccionario
contactos = dict()

#Itero 5 veces para que el usuario pueda ingresar 5 nombres con sus respectivos números de teléfono
for n in range(1, 6):
    nombre = input(f"Ingrese su el {n} nombre: ")
    telefono = input("Ingrese el número de teléfono: ")
    #Agrego la clave como el valor al diccionario
    contactos[nombre] = telefono

#Imprimo por pantalla el diccionario
print(contactos)