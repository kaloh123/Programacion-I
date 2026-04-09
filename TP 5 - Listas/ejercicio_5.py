alumnos_presentes = ["Diego", "Mateo", "Juan", "Iara", "Romina", "Nicolas", "Vanesa", "Martin"]

while True:

    print(f"\nLista actual de alumnos: {alumnos_presentes}")
    print("""   
        Menú
    1 - Agregar alumno
    2 - Eliminar alumno
    3 - Salir""")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        agregar_alumno = input("Ingrese el nombre del alumno: ")

        if not agregar_alumno.capitalize() in alumnos_presentes:
            alumnos_presentes.append(agregar_alumno.capitalize())
            print(f"El alumno {agregar_alumno.capitalize()} fue agregado a la lista correctamente!")
        else:
            print(f"El alumno {agregar_alumno.capitalize()} ya se encuentra en la lista!")
    
    if opcion == "2":

        eliminar_alumno = input("Ingrese el nombre del alumno: ")

        if eliminar_alumno.capitalize() in alumnos_presentes:
            alumnos_presentes.remove(eliminar_alumno.capitalize())
            print(f"El alumno {eliminar_alumno.capitalize()} fue eliminado de la lista correctamente!")
        else:
            print(f"El alumno {eliminar_alumno.capitalize()} no se encuentra en la lista!")

    if opcion == "3":
        break

print("Saliendo del sistema...")

    