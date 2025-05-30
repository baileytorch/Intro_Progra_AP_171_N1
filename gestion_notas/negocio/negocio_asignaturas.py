import os
from data.asignaturas import asignaturas
from data.crear_data import guardar_data

# READ DATA
def obtener_listado_asignaturas():    
    print()
    print('Listado de Asignaturas')
    print('======================')
    contador = 0
    for asignatura in sorted(asignaturas):
        contador += 1
        print(f'[{contador}] {asignatura}')

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
    pass

# DELETE DATA
def eliminar_asignatura():
    pass