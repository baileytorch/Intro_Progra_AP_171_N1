from data.leer_data import listado_data,obtener_indice_data
from data.crear_data import guardar_data
from data.docentes import docentes

# READ DATA
def obtener_listado_docentes():    
    print()
    print('Listado de Docentes')
    print('===================')
    lista = listado_data('docentes.py')
    contador = 0
    for data in sorted(lista):
        contador += 1
        print(f'[{contador}] {data}')

# CREATE DATA
def guardar_nuevo_docente():
    obtener_listado_docentes()
    nuevo_docente = input('Ingrese nuevo docente: ')
    docentes.append(nuevo_docente.title())
    guardar_data('docentes',docentes,'docentes.py')

# UPDATE DATA
def actualizar_docente():
    obtener_listado_docentes()
    busqueda = input("Ingrese asignatura a buscar: ")
    indice_docente = obtener_indice_data('docentes.py', busqueda)

    if indice_docente is not None:
        docente_modificado = input("Ingrese nuevo nombre de asignatura: ")
        docentes[indice_docente] = docente_modificado.title()
        guardar_data('docentes',docentes,'docentes.py')
    else:
        print('Docente NO encontrado')

# DELETE DATA
def eliminar_docente():
    obtener_listado_docentes()
    busqueda = input("Ingrese asignatura a buscar: ")
    indice_docente = obtener_indice_data('docentes.py', busqueda)

    if indice_docente is not None:
        docentes.pop(indice_docente)
        guardar_data('docentes',docentes,'docentes.py')
    else:
        print('Docente NO encontrado')