import os

def guardar_data(nombre_lista, lista_data, nombre_archivo):
    try:
        archivo_datos = nombre_archivo
        ubicacion_archivo = os.path.join('gestion_notas/data', archivo_datos)
        ubicacion_archivo = os.path.abspath(ubicacion_archivo)
        ubicacion_archivo = os.path.realpath(ubicacion_archivo)    
        archivo = open(f"{ubicacion_archivo}", "w+")
        archivo.write(f'{nombre_lista} = {lista_data}')
        archivo.close()
        return 'Guardado Exitoso'
    except:
        print('Archivo inaccesible...')