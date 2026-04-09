ventas = [
    [10, 5, 8, 12, 7, 4, 9],  # Producto 1 (7 días)
    [20, 15, 18, 22, 17, 14, 19], # Producto 2
    [5, 2, 4, 6, 3, 1, 5],     # Producto 3
    [12, 12, 12, 12, 12, 12, 12]  # Producto 4
]

totales_por_producto = []
suma_producto = 0

for i in range(len(ventas)):
    suma_producto = sum(ventas[i])
    totales_por_producto.append(suma_producto)
    print(f"Total vendido producto {i+1}: {suma_producto}")

max_ventas = totales_por_producto[0]
producto_ganador = 1

for i in range(len(totales_por_producto)):
    if totales_por_producto[i] > max_ventas:
        max_ventas = totales_por_producto[i]
        producto_ganador = i + 1

print("-" * 50)
print(f"El producto más vendido fue el {producto_ganador} con {max_ventas} unidades")
print("-" * 50)

max_dia_ventas = 0
dia_ganador = 0

for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]

    print(f"Ventas totales del dia {j+1}: {suma_dia}")

    if suma_dia > max_dia_ventas:
        max_dia_ventas = suma_dia
        dia_ganador = j + 1

print(f"\nEl día con mayores ventas fue el día {dia_ganador} con un total de {max_dia_ventas}.")