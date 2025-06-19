from data.asignaturas import asignaturas
from data.docentes import docentes

def listado_data(nombre_archivo):
    lista = []
    try:
        if nombre_archivo == 'asignaturas.py':
            lista = asignaturas
        elif nombre_archivo == 'docentes.py':
            lista = docentes
    except:
        print('Archivo no encontrado...')
    
    return lista

def obtener_indice_data(nombre_archivo,busqueda):
    try:
        lista = listado_data(nombre_archivo)

        if len(lista) > 0:    
            indice = None
            for i in range(len(lista)):
                if busqueda.lower() in lista[i].lower():
                    indice = i
            return indice
    except:
        print('Lista de datos NO encontrada...')