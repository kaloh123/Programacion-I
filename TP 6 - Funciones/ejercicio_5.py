# Definición de funciones
def segundos_a_horas(segundos):

    horas = segundos/3600

    return horas


# Programa principal
segundos = int(input("Ingrese la cantidad de segundos a pasar: "))

print(f"{segundos} segundos a horas son: {segundos_a_horas(segundos):.1f}h")