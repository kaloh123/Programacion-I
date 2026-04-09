alumnos = ["DIEGO", "IARA", "MORA", "LUCIA", "MARTIN", "LAUTARO", "JONATHAN", "POLO", "MARCO", "MARIANO"]

while True:
    print("""
    MENU
1 - UBICAR ALUMNO
2 - SALIR
""")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre_alumno = input("Ingrese el nombre del alumno (en mayúsculas o sin tildes): ")

        if nombre_alumno.upper() in alumnos:
            print("-" * 50)
            print("El alumno se encuentra en la lista!")
            posicion = alumnos.index(nombre_alumno.upper())
            print(f"Su posición en la lista es la {posicion}")
            print("-" * 50)

        else:
            print("-" * 50)
            print("El alumno no se encuentra en la lista!")

    if opcion == "2":
        break

print("Saliendo del sistema...")

