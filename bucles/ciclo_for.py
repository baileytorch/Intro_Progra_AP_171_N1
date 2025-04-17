# Ciclo FOR se usa generalmente para ITERAR elementos

juegos = ["Dota 2","Counter Strike","Mario Party 9","Hades"]
print()
for juego in juegos:
    print(juego)
    
numeros = [10,20,30,40,50]
print()
for numero in numeros:
    resultado = numero * numero
    print(f"{numero}*{numero}={resultado}")

print()
sumatoria = 0
for num in numeros:
    sumatoria = num + sumatoria
print(f"La sumatoria de {numeros} = {sumatoria}")

print()
for numero in range(11):
    print(numero)
    
print()
for numero in range(5,26):
    print(numero)
    
print()
lista_numeros = []
for numero in range(5,51,5):
    lista_numeros.append(numero)
print(lista_numeros)

print()
for num in enumerate(lista_numeros):
    indice = num[0]
    valor = num[1]
    print(f"El índice es: {indice}. El valor es: {valor}")
print()
print(type(enumerate(lista_numeros)))