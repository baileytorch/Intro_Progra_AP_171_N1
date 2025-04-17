# El ciclo WHILE (mientras) nls permite ejecutar una seri de acciones
# mientras una condición lógica sea VERDADERA

contador_str = input("Ingrese un número entero menor a 50:")
contador_int = int(contador_str)

while contador_int < 50:
    contador_int = contador_int + 1
    print(f"Su contador es: {contador_int}")

print(f"Ciclo terminado, Ud. ingresó el número: {contador_str}")