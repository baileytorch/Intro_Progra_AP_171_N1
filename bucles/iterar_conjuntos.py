cervezas = {"Royal Guard","Stella Artois","Coors","Heineken","Dolbek"}
print()
for chela in cervezas:
    print(f"Lo más hermoso de la comida: {chela}")
    
numeros = {10,20,30,40,50}
print()
for numero in numeros:
    resultado = numero * numero
    print(f"{numero}*{numero}={resultado}")

print()    
print(type(numeros))
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")