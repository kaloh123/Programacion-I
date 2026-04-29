# Definición de funciones
def calcular_area_circulo(radio):
    
    pi = 3.14
    area_circulo = pi * (radio)**2

    return area_circulo

def calcular_perimetro_circulo(radio):

    pi = 3.14
    perimetro_circulo = 2 * pi * radio

    return perimetro_circulo

#Programa principal
radio = int(input("Ingrese el radio del círculo (en cm): "))

print(f"El área del círculo es de: {calcular_area_circulo(radio):.2f}cm")
print(f"El perímetro del círculo es de: {calcular_perimetro_circulo(radio):.2f}cm")
