lista_productos = []
#El usuario ingrese los 5 productos a la lista
print("Cargue 5 productos a la lista")
for i in range(1,6):
    producto = input(f"Ingrese el {i} producto: ")
    lista_productos.append(producto.upper())
    #Se ordena la lista alfabeticamente
    lista_productos.sort()

    
#Hago un bucle infinito
while True:
    #Muestro el menú con sus opciones
    print(f"\nLista actual: {lista_productos}")
    print("""Menú
    1- Eliminar producto
    2- Salir""")
    
    opcion = input("Seleccione una opción: ")
    #Opción para borrar productos
    if opcion == "1":

        borrar_producto = input("¿Qué producto desea borrar? ")
        #Si el producto que ingresó el usuario se encuentra en la lista, se cumple la condición
        if borrar_producto.upper() in lista_productos:
            #Borro el producto y le agrego .upper para que coincida con el producto de la lista
            lista_productos.remove(borrar_producto.upper())
            print(f"Producto {borrar_producto} fue eliminado con éxito!")
        else:
            print("Ese producto no está en la lista")
    #Opción para salir del programa
    elif opcion == "2":
        break

print(f"Estos son sus productos {lista_productos}")
print("Saliendo del sistema!")
