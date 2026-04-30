frase = input("Ingrese una frase: ").lower()

#Convierto la frase en una lista de palabras
palabras = frase.split()

#Paso la lista a un set y así se eliminan los duplicados
palabras_unicas = set(palabras)

#Creo el diccionario
recuento = dict()

for palabra in palabras:
    if palabra in recuento:
        #Si la palabra ya está en el diccionario se suma 1
        recuento[palabra] += 1
    else:
        #Si es la primera vez que la palabra aparece, se crea con un valor 1
        recuento[palabra] = 1

#Imprimo por pantalla los resultados
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")