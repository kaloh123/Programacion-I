import random

lista_azar = []
lista_pares = []
contador_pares = 0
lista_impares = []
contador_impares  =0

for cant_num in range(0, 15):
    lista_azar.append(random.randint(1,100))

for num_lista in range(len(lista_azar)):
    if lista_azar[num_lista] % 2 == 0:
        lista_pares.append(lista_azar[num_lista])
        contador_pares += 1
    else:
        lista_impares.append(lista_azar[num_lista])
        contador_impares += 1


print(f"{lista_azar}")
print(f"Lista pares {lista_pares} tiene {contador_pares} números")
print(f"Lista impares {lista_impares} tiene {contador_impares} números")