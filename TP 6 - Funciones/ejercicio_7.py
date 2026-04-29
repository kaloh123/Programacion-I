# Definición de funciones
def operaciones_basicas(a, b):

    suma = a + b
    resta = a - b
    multi = a * b
    if b != 0:
        div = a / b
    else:
        div = 0

    return (suma, resta, multi, div)


# Programa principal
num1 = int(input("Ingrese el primero número: "))
num2 = int(input("Ingrese el segundo número: "))

tupla_resultados = operaciones_basicas(num1, num2)

print(f"La suma es: {tupla_resultados[0]}")
print(f"La resta es: {tupla_resultados[1]}")
print(f"La multiplicación es: {tupla_resultados[2]}")
print(f"La división es: {tupla_resultados[3]}")