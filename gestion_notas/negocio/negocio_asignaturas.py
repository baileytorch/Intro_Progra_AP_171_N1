from data.crear_data import guardar_data
from data.leer_data import listado_data,obtener_id_data
from data.asignaturas import asignaturas

# READ DATA
def obtener_listado_asignaturas():    
    print()
    print('Listado de Asignaturas')
    print('======================')
    lista = listado_data('asignaturas.py')
    contador = 0
    for data in sorted(lista):
        contador += 1
        print(f'[{contador}] {data}')

# READ DATA
def obtener_asignatura_individual():
    asignatura_encontrada = 'asignatura NO encontrada'
    busqueda = input("Ingrese asignatura a buscar: ")
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            asignatura_encontrada = asignatura
    return asignatura_encontrada

# CREATE DATA
def guardar_nueva_asignatura():
    obtener_listado_asignaturas()
    nueva_asignatura = input('Ingrese nueva asignatura: ')
    asignaturas.append(nueva_asignatura.title())
    guardar_data('asignaturas',asignaturas,'asignaturas.py')
    
# UPDATE DATA
def actualizar_asignatura():
    obtener_listado_asignaturas()
    busqueda = input("Ingrese asignatura a buscar: ")
    indice_asignatura = obtener_id_data('asignaturas.py', busqueda)

    if indice_asignatura is not None:
        asignatura_modificada = input("Ingrese nuevo nombre de asignatura: ")
        asignaturas[indice_asignatura] = asignatura_modificada.title()
        guardar_data('asignaturas',asignaturas,'asignaturas.py')
    else:
        print('Asignatura NO encontrada')

# DELETE DATA
def eliminar_asignatura():
    pass