#Creo el diccionario
alumnos = dict()

for n in range(1, 4):
    nombre_alumno = input(f"Ingrese el nombre del {n} alumno: ").upper()
    
    #Creo una lista temporal para poder guardar las notas y después pasarla a tupla
    notas_temporales = []

    for nota in range(1, 4):
        nota_alumno = int(input(f"Ingrese la nota {nota} del alumno {nombre_alumno}: "))

        #Agrego la nota del alumno a la lista temporal
        notas_temporales.append(nota_alumno)

        #Convierto la lista a tupla y le asigno el valor de esta a la clave correspondiente que en este caso seria el nombre de cada alumno
        alumnos[nombre_alumno] = tuple(notas_temporales)

    #Recorro el diccionario 
for nombre, notas in alumnos.items():
    
    promedio = sum(notas) / len(notas)

    #Imprimo por pantalla el promedio de cada alumno
    print("-" * 40)
    print("Promedio:")
    print(f"Alumno {nombre} - Promedio: {promedio:.2f}")

#Imprimo por pantalla las notas de los alumnos
print("-" * 60)
print("Notas de los alumnos:")
print(alumnos)