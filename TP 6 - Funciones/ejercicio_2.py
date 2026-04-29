# Definicion de funciones
def saludar_usuario(nombre):
    saludar = f"Hola {nombre}!"
    return saludar


# Programa principal
nombre_usuario = input("Ingrese su nombre: ")

print(saludar_usuario(nombre_usuario))