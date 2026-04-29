# Definición de funciones
def celsius_a_fahrenheit(celsius):
    a_fahrenheit = (celsius * (9/5)) + 32

    return a_fahrenheit

# Programa principal
celsius = float(input("Ingrese los grados (en celsius) a convertir: "))

print(f"°{celsius} celsius son °{celsius_a_fahrenheit(celsius):.2f} fahrenheit")