import math
# Funciones con números

numeros = [4,6,2,9,25]

print(f"El número mayor es: {max(numeros)}")
print(f"El número menor es: {min(numeros)}")

numero = 12.3456
print()
print(f"Redondear el decimal {numero} = {round(numero)}")
print(f"Redondear el decimal {numero} a 2 decimales = {round(numero,2)}")
print(f"Truncar el decimal {numero} = {math.trunc(numero)}")
print(f"Aproximar al entero superior el decimal {numero} = {math.ceil(numero)}")
print(f"Valor absoulto de -45 = {math.fabs(-45)}")
print(f"Raíz cuadrada de 9 = {math.sqrt(9)}")
print(f"Sumatoria de 4+6+2+9+25 = {math.fsum(numeros)}")