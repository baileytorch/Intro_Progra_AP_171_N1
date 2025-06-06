from data.leer_data import listado_data
from data.crear_data import guardar_data
from data.docentes import docentes

# READ DATA
def obtener_listado_docentes():    
    print()
    print('Listado de Docentes')
    print('===================')
    listado_data('docentes.py')

# CREATE DATA
def guardar_nuevo_docente():
    obtener_listado_docentes()
    nuevo_docente = input('Ingrese nuevo docente: ')
    docentes.append(nuevo_docente.title())
    guardar_data('docentes',docentes,'docentes.py')
