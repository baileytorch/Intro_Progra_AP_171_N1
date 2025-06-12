from data.asignaturas import asignaturas
from data.docentes import docentes

def listado_data(nombre_archivo):
    lista = []
    if nombre_archivo == 'asignaturas.py':
        lista = asignaturas
    elif nombre_archivo == 'docentes.py':
        lista = docentes
    return lista