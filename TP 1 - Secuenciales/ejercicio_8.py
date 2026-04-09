altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilos: "))

imc = (peso / (altura ** 2))

print(f"Su IMC es de {imc}")