#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#Agrego las frutas solicitadas, ingresando la clave y su respectivo valor, en este caso la fruta y el precio
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#Imprimo por pantalla el diccionario actualizado
print(precios_frutas)

#Ejercicio 2
#Actualizo los precios de las frutas solicitadas
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

#Imprimo por pantalla el diccionario actualizado
print(precios_frutas)

#Ejercicio 3
#Extraigo solo las claves del diccionario precios_frutas y lo transformo en una lista
claves_frutas = precios_frutas.keys()
lista_claves_frutas = list(claves_frutas)

#Imprimo por pantalla la lista de frutas sin sus precios
print(lista_claves_frutas)

