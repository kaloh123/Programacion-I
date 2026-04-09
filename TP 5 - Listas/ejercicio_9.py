tablero = [
    ["-" ,"-" ,"-"], #Fila 0
    ["-" ,"-" ,"-"], #Fila 1
    ["-" ,"-" ,"-"] #Fila 2
]

turno = "X"
jugadas = 0

#El programa se ejecuta mientras haya casillas vacias (max 9)
while jugadas < 9:

    #Se muestra el tablero
    print("\n--- TABLERO ACTUAL ---")
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ") 
        print() 
    print("----------------------")

    #Se le pide la posición tanto de la fila como de la columna al usuario
    print(f"Turno del jugador: {turno}")
    fila = int(input("Seleccione una fila (0, 1, 2): "))
    columna = int(input("Seleccione una columna (0, 1, 2): "))

    if fila <= 2 and fila <= 0 and columna <= 2 and columna >= 0:
        if tablero[fila][columna] == "-":
            #Se cambia el valor en la matriz por el turno que sea actualmente X o O
            tablero[fila][columna] = turno
            jugadas += 1

            #Cambio de turno
            if turno == "X":
                turno = "O"
            else:
                turno = "X"
        
        else:
            print("Error! La casilla está ocupada!")

    else:
        print("Valor fuera de rango (0, 1, 2)")

print("\n--- TABLERO FINAL ---")
for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ") 
        print() 
print("Fin de la partida!")
    

