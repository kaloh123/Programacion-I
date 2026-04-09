lista_notas = [7,5,5,6,10,3,8,4,1,9]
#Variables para comparar notas más altas y más bajas
nota_mas_alta = lista_notas[0]
nota_mas_baja= lista_notas[0]
#Suma para poder realizar el promedio
suma = 0
#Cantidad de notas para el promedio
cant_notas = len(lista_notas)

#Recorre cada una de las notas de la ista
for i in range(len(lista_notas)):
    #Suma las notas para poder realizar el promedio
    suma += lista_notas[i]

    #Condición para ver cuál es la nota más alta
    if lista_notas[i] > nota_mas_alta:
        nota_mas_alta = lista_notas[i]

    #Condición para ver cuál es la nota más baja
    if lista_notas[i] < nota_mas_baja:
        nota_mas_baja = lista_notas[i]

#Operación promedio
promedio = (suma) / cant_notas

print(f"Lista completa: {lista_notas}")
print(f"El promedio de notas es: {promedio}")
print(f"La nota más alta es: {nota_mas_alta}")
print(f"La nota más baja es: {nota_mas_baja}")