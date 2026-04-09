puntajes = [450, 1200, 875, 990, 300, 1500, 640]

puntaje_mas_alto = puntajes[0]
puntaje_mas_bajo = puntajes[0]

ranking = sorted(puntajes, reverse = True)

for puntos in ranking:
    if puntos > puntaje_mas_alto:
        puntaje_mas_alto = puntos
    elif puntos < puntaje_mas_bajo:
        puntaje_mas_bajo = puntos

for i in range(len(ranking)):
    if ranking[i] == 990:
        puntaje_solicitado = i + 1


print(f"El ranking es el siguiente: {ranking}")
print(f"El mayor puntaje es de: {puntaje_mas_alto} pts")
print(f"El menor puntaje es de: {puntaje_mas_bajo} pts")
print(f"El puntaje 990 se encuentra en el puesto: {puntaje_solicitado} del ranking")


