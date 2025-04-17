# Tipo de dato: TEXTO
# Texto de una sola línea
texto_1 = 'Texto 1: texto de una línea'
texto_2 = "Texto 2: texto de una línea"

# Texto de múltiples líneas
texto_3 = '''Texto 3:
texto múltiple 
línea'''

print(texto_1)
print(texto_2)
print(texto_3)

# Tipo de dato: NUMÉRICO
# Enteros, integers INT
numero_entero = 49
numero_prueba = '56'
print(numero_entero)
print(type(numero_entero))

# Decimales, float FLOAT DEC
numero_decimal = 49.5
print(numero_decimal)
print(type(numero_decimal))

# Datos LÓGICOS, boolean BOOL
dato_booleano = True
print(dato_booleano)
print(type(dato_booleano))

nombre = "Erick Bailey"
edad = 49
print("Hola estimado "+ nombre)
print("Hola estimado", nombre)

print("Hola estimado "+ nombre + ", tienes unos maravillosos " + str(edad) + " años.")
print(f"Hola estimado {nombre}, tienes unos maravillosos {edad} años")

print(numero_entero+int(numero_prueba))
print(numero_entero*numero_prueba)