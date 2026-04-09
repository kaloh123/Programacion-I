lista_numeros = [1, 2, 3, 4, 5, 6, 7]

#El ultimo elemento de la lista + todos los elementos hasta el anteúltimo
#[lista_numeros[-1]] es el ultimo elemento de la lista, está metido en una lista propia
#lista_numeros[:-1] esto quiere decir, desde el principio hasta el anteúltimo
lista_numeros = [lista_numeros[-1]] + lista_numeros[:-1]

print(lista_numeros)