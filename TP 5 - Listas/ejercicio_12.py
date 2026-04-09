numeros = []

#El usuario ingresa los 8 números enteros
for i in range(0,8):
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)

#Ordeno la lista para que los números sean de menor a mayor
numeros_ordenados_menor_mayor = sorted(numeros)
#Ordeno la lista para que los números sean de mayor a menor con la función reverse
numeros_ordenados_mayor_menor = sorted(numeros, reverse = True)

print(f"Lista original: {numeros}")
print(f"Lista ordenada de menor a mayor: {numeros_ordenados_menor_mayor}")
print(f"Lista ordenada de mayor a menor: {numeros_ordenados_mayor_menor}")