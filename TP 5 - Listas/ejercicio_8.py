notas_alumnos = [
    [8, 7, 10], #Estudiante 0
    [5, 4, 6], #Estudiante 1
    [9, 9, 8], #Estudiante 2
    [7, 6, 5], #Estudiante 3 
    [10, 8, 9] #Estudiante 4 
]

print("-" * 30)
print("Promedio de cada estudiante")

for i in range(len(notas_alumnos)):
    #Es la fila de notas del estudiante del indice i
    suma_notas = sum(notas_alumnos[i])
    promedio = suma_notas / 3
    print(f"Estudiante {i+1}: {promedio:.2f}")

print("-" * 30)
print("Promedio por materia")

#Como son 3 materias, hago el bucle 3 veces
for j in range(3):
    suma_materia = 0
    #Se chequea cada estudiante para sacar su nota de cada materia 
    for estudiante in notas_alumnos:
        suma_materia += estudiante[j]

    promedio_materia = suma_materia / 5
    print(f"Materia {j+1}: {promedio_materia:.2f}")
