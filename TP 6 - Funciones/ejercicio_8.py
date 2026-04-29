# Definición de funciones
def calcular_peso(peso, altura):
    
    imc = peso / (altura)**2

    return imc


# Programa principal
peso = int(input("Ingrese su peso (en kg): "))
altura =float(input("Ingrese su altura (en mts): "))

print(f"Su IMC es de: {calcular_peso(peso, altura):.2f}")