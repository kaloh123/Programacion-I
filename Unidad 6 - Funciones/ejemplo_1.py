#definicion de funciones
def obtener_resto(num1, num2):
    return num1 - num2 * (num1 // num2) # en reemplazo de %

def esmultiplo(num1, num2):
    return obtener_resto(num1, num2) == 0

#programa principal
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resto = obtener_resto(a, b)

print(f"El resto entre {a} y {b} es: {resto}")
if esmultiplo(a, b):
    print(f"{a} es múltiplo de {b}")
else:
    print(f"{a} no es múltiplo de {b}")