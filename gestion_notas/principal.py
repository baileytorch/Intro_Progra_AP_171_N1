import os
from data.asignaturas import asignaturas

def obtener_listado_asignaturas():    
    print()
    print('Listado de Asignaturas')
    print('======================')
    contador = 0
    for asignatura in sorted(asignaturas):
        contador += 1
        print(f'[{contador}] {asignatura}')

def obtener_asignatura_individual():
    asignatura_encontrada = 'asignatura NO encontrada'
    busqueda = input("Ingrese asignatura a buscar: ")
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            asignatura_encontrada = asignatura
    return asignatura_encontrada

def guardar_nueva_asignatura():
    obtener_listado_asignaturas()
    nueva_asignatura = input('Ingrese nueva asignatura: ')
    asignaturas.append(nueva_asignatura.title())
    
    file = 'asignaturas.py'
    location = os.path.join('gestion_notas/data', file)
    location = os.path.abspath(location)
    location = os.path.realpath(location)    
    archivo = open(f"{location}", "w+")
    archivo.write(f'asignaturas = {asignaturas}')
    archivo.close()    
    obtener_listado_asignaturas()

guardar_nueva_asignatura()