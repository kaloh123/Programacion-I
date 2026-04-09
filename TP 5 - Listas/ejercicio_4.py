datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

lista_sin_repetidos = []

#Recorro la lista de datos
for i in range(len(datos)):
    #Si el valor no se encuentra en la lista sin repetidos, este se agrega a la lista
    if not datos[i] in lista_sin_repetidos: 
        lista_sin_repetidos.append(datos[i])

print(f"Lista sin repetidos {lista_sin_repetidos}")