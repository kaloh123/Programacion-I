# Definición de funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        multiplicacion = numero * i
        print(f"{numero} x {i} es: {multiplicacion}")

# Programa principal
numero = int(input("Ingrese un número: "))

print(tabla_multiplicar(numero))