# Podemos usar herramientas con nuestras variables... f es para formatear... 
# del permite borrar variables

nombre_completo = input("Ingrese su nombre completo: ")
saludar = f"Buen día don(a) {nombre_completo}, ¿Cómo estás?"
del saludar
# print(saludar)

texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Ut nec velit non magna placerat eleifend a ac ante. Etiam id mi sed elit fringilla tempor. 
Morbi pretium, nibh in feugiat mattis, orci neque suscipit massa, 
vel suscipit ex ex sed libero. Aliquam id volutpat arcu. 
Nunc pharetra felis et commodo gravida. Nullam euismod mollis diam eu ullamcorper. 
Integer non hendrerit mi. Curabitur fringilla mauris vitae eros congue, 
ut cursus felis condimentum. Mauris faucibus justo quis nunc interdum sodales. 
Pellentesque eros est, pulvinar vitae justo id, 
sagittis fermentum nisl. In facilisis ipsum quis viverra pretium.
"""

# IN permite buscar un texto dentro de otro, devuelve TRUE si encuentra el texto
# devuelve FALSE si no lo encuentra
busqueda_in = input("Ingrese su texto de búsqueda con IN: ")
busqueda_texto = busqueda_in in texto
print(busqueda_texto)

# FIND permite buscar un texto dentro de otro y 
# entrega la primera posición de la primera coincidencia de texto
# entrega -1 si no lo encuentra
busqueda_find = input("Ingrese su texto de búsqueda: ")
busqueda_2 = texto.find(busqueda_find)
print(f"Buscando con FIND: {busqueda_2}")

# RFIND permite buscar un texto dentro de otro y 
# entrega la primera posición de la primera coincidencia de texto
# entrega -1 si no lo encuentra
nueva_busqueda_2 = texto.rfind(busqueda_find)
print(f"Buscando con RFIND: {nueva_busqueda_2}")

# COUNT permite buscar un texto dentro de otro y 
# entrega la cantidad de ocurrencias del texto
# entrega 0 si no lo encuentra
numero_ocurrencias = texto.count(busqueda_find)
print(f"Buscando con COUNT: {numero_ocurrencias}")

# INDEX permite buscar un texto dentro de otro y 
# entrega el índice de la primera posición de la primera coincidencia de texto
# entrega ERROR si no lo encuentra
busqueda_index = input("Ingrese su texto de búsqueda con INDEX: ")
busqueda_3 = texto.index(busqueda_index)
print(f"Buscando con INDEX: {busqueda_3}")