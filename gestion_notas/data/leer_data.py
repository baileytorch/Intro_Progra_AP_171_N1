from data.asignaturas import asignaturas
from data.docentes import docentes

def listado_data(nombre_archivo):
    if nombre_archivo == 'asignaturas.py':
        lista = asignaturas
    elif nombre_archivo == 'docentes.py':
        lista = docentes

    contador = 0
    for data in sorted(lista):
        contador += 1
        print(f'[{contador}] {data}')