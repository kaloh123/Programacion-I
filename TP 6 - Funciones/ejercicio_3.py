# Definicion de funciones 
def informacion_personal(nombre, apellido, edad, residencia):
    
    presentacion = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
    
    return presentacion


# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("¿Dónde vive? ")

print(informacion_personal(nombre, apellido, edad, residencia))