print("Ingrese True o False")
variable_booleana_str = input()
variable_booleana = bool(variable_booleana_str)

if variable_booleana == True:
    print("Verdadero")
else:
    print("Falso")

# Métodos para convertir tipos de datos
texto = '25'
decimal = 45
boleana = False
entero = 40.5

print(f"Variable de tipo {type(texto)}")
print(f"Variable de tipo {type(decimal)}")
print(f"Variable de tipo {type(boleana)}")
print(f"Variable de tipo {type(entero)}")

texto_intero = int(texto) # Convierte a INTEGER int
boleano_texto = str(boleana) # Convierte a STRING str
entero_decimal = float(decimal) # Convierte a DECIMAL float

print("")
print(f"Variable de tipo {type(texto_intero)}")
print(f"Variable de tipo {type(boleano_texto)}")
print(f"Variable de tipo {type(entero)}")