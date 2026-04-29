# Definción de funciones
def calcular_promedio(a, b, c):

    promedio = (a + b + c) / 3

    return promedio

# Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

print(f"El promedio entre los números es: {calcular_promedio(num1, num2, num3):.2f}")