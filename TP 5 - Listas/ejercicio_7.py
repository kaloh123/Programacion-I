temp_semanal = [
    [12, 25],#Lunes
    [10, 22],#Martes
    [14, 28],#Miércoles
    [15, 30],#Jueves
    [11, 24],#Viernes
    [13, 26],#Sábado
    [16, 29]#Domingo
]

temp_minimas = 0
temp_maximas = 0

mayor_amplitud = 0
dia_mayor_amplitud = 0

for temp in temp_semanal:
    temp_minimas += temp[0] #El primer valor es la mínima
    temp_maximas += temp[1] #El segundo valor es la máxima

promedio_min = temp_minimas / len(temp_semanal)
promedio_max = temp_maximas / len(temp_semanal)

print(f"Promedio de mínimas: {promedio_min:.2f}")
print(f"Promedio de máximas: {promedio_max:.2f}")

for i in range(len(temp_semanal)):
    amplitud_actual = temp_semanal[i][1] - temp_semanal [i][0]

    if amplitud_actual > mayor_amplitud:
        mayor_amplitud = amplitud_actual
        dia_mayor_amplitud = i + 1  

print(f"La mayor amplitud térmica fue de {mayor_amplitud} grados, el día {dia_mayor_amplitud}.")
