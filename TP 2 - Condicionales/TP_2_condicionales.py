#1
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

#2
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    "Desaprobado"

#3
numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

#5
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6
consumo_kwh = int(input("Ingrese su consumo energético mensual: "))

if consumo_kwh < 150:
    print("Consumo bajo")
elif consumo_kwh >= 150 and consumo_kwh <= 300:
    print("Consumo medio")
elif consumo_kwh > 300 and consumo_kwh <= 500:
    print("Consumo alto")
elif consumo_kwh > 500:
    print("Considere medidas de ahorro energético")

#7
frase_palabra = input("Ingrese una frase o palabra: ")

vocales = "aeiouAEIOU"

if frase_palabra[-1] in vocales:
    frase_palabra_final = frase_palabra + "!"
    print(frase_palabra_final)
else:
    print(frase_palabra)

#8
nombre = input("Ingrese su nombre: ")

print("""
1. Si quiere su nombre en mayúsculas
2. Si quiere su nombre en minúsculas
3. Si quiere su nombre con la primera letra mayúscula.
""")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    nombre = nombre.upper()
    print(nombre)

elif opcion == 2:
    nombre = nombre.lower()
    print(nombre)

elif opcion == 3:
    nombre = nombre.title()
    print(nombre)

#9
magnitud_terremoto = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud_terremoto < 3:
    print("Muy leve \nimperciptible")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve \nligeramente perciptible")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print("Moderado \nsentido por personas, pero generalmente no causa daños")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte \npuede causar daños en estructuras débiles")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print("Muy fuerte \npuede causar daños significativos")
else:
    print("Extremo \npuede causar graves daños a gran escala")

#10 
hemisferio = int(input("¿En qué hemisferio se encuentra? "
                "\n1- hemisferio norte " 
                "\n2- hemisferio sur " 
                "\nSeleccione el hemisferio "))

mes = int(input("¿En qué mes del año se encuentra? " 
                "\n1- Enero " 
                "\n2- Febrero "
                "\n3- Marzo "
                "\n4- Abril " 
                "\n5- Mayo " 
                "\n6- Junio " 
                "\n7- Julio " 
                "\n8- Agosto " 
                "\n9- Septiembre " 
                "\n10- Octubre " 
                "\n11- Noviembre " 
                "\n12- Diciembre " 
                "\nSeleccione el mes "))

dia = int(input("Ingrese el dia del mes "))

if hemisferio == 1 :
    if mes == 12 and (dia >= 21 and dia < 31) or mes == 1 and (dia >= 1 and dia <= 31) or mes == 2 and (dia >= 1 and dia <= 28) or mes == 3 and (dia >= 1 and dia <= 20):
        print("Usted está en invierno")
    elif mes == 3 and (dia >= 21 and dia < 31) or mes == 4 and (dia >= 1 and dia <= 30) or mes == 5 and (dia >= 1 and dia <= 31) or mes == 6 and (dia >= 1 and dia <= 20):
        print("Usted está en primavera")
    elif mes == 6 and (dia >= 21 and dia < 30) or mes == 7 and (dia >= 1 and dia <= 31) or mes == 8 and (dia >= 1 and dia <= 31) or mes == 9 and (dia >= 1 and dia <= 20):
        print("Usted está en verano")
    elif mes == 9 and (dia >= 21 and dia < 30) or mes == 10 and (dia >= 1 and dia <= 31) or mes == 11 and (dia >= 1 and dia <= 30) or mes == 12 and (dia >= 1 and dia <= 20):
        print("Usted está en otoño")

elif hemisferio == 2 :
    if mes == 12 and (dia >= 21 and dia < 31) or mes == 1 and (dia >= 1 and dia <= 31) or mes == 2 and (dia >= 1 and dia <= 28) or mes == 3 and (dia >= 1 and dia <= 20):
        print("Usted está en verano")
    elif mes == 3 and (dia >= 21 and dia < 31) or mes == 4 and (dia >= 1 and dia <= 30) or mes == 5 and (dia >= 1 and dia <= 31) or mes == 6 and (dia >= 1 and dia <= 20):
        print("Usted está en otoño")
    elif mes == 6 and (dia >= 21 and dia < 30) or mes == 7 and (dia >= 1 and dia <= 31) or mes == 8 and (dia >= 1 and dia <= 31) or mes == 9 and (dia >= 1 and dia <= 20):
        print("Usted está en invierno")
    elif mes == 9 and (dia >= 21 and dia < 30) or mes == 10 and (dia >= 1 and dia <= 31) or mes == 11 and (dia >= 1 and dia <= 30) or mes == 12 and (dia >= 1 and dia <= 20):
        print("Usted está en primavera")