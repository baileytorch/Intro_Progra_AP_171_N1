# Datos compuestos son COLECCIONES de elementos o datos que pueden pertencer a una variable

# LISTAS, colección ORDENADA de elementos mutables
lista = ["Erick Bailey", 49, True]
print(lista)
print(type(lista))
print(lista[0])
lista[0]="Erick Bailey Rebolledo"
print(lista)
lista.append("Torch")
print(lista)

# DICCIONARIOS, colecciones ORDENADA de pares de elementos mutables
diccionario = {
    "nombre":"Erick Bailey",
    "edad": 49,
    "Es profesor?": True
}
print(diccionario)
print(type(diccionario))
print(diccionario["nombre"])
diccionario["nombre"]="Erick Bailey Rebolledo"
print(diccionario)
# print(diccionario.keys())
# diccionario.clear()
# print(f"Diccionario: {diccionario}")

# TUPLAS, coleccion ordenada inmutable de elementos
tupla = ("Erick Bailey", 49, True)
print(tupla)
print(type(tupla))

print(tupla[0])
# tupla[0] = "Erick Bailey Rebolledo"

# CONJUNTOS, coleccion desordenada de elementos
conjunto = {"Erick Bailey", 49, True}
print(conjunto)
print(type(conjunto))
conjunto.add(78)
print(conjunto)
conjunto.pop()
print(conjunto)
