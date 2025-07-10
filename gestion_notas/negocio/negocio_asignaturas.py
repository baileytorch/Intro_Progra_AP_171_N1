from data.crear_data import guardar_data
from data.leer_data import listado_data, obtener_indice_data
from data.asignaturas import asignaturas
from data.conexion import leer_datos, insertar_datos
from prettytable import PrettyTable

# READ DATA


def obtener_listado_asignaturas():
    print()
    print('Listado de Asignaturas')
    print('======================')
    consulta = f'''
        SELECT id_asignatura,codigo_asig,nombre_asig 
        FROM asignaturas
        WHERE habilitado = 1
    '''
    tabla_asignaturas = PrettyTable()
    tabla_asignaturas.field_names = [
        'N°', 'Código Asignatura', 'Nombre Asignatura']
    listado_asignaturas = leer_datos(consulta)
    if listado_asignaturas != None:
        for asignatura in listado_asignaturas:
            tabla_asignaturas.add_row(asignatura)  # type: ignore
    else:
        print('No se han encontrado datos.')
    print(tabla_asignaturas)

# CREATE DATA


def guardar_nueva_asignatura():
    obtener_listado_asignaturas()
    cod_asignatura = input('Ingrese código nueva asignatura: ')
    nombre_asignatura = input('Ingrese nombre nueva asignatura: ')
    desc_asignatura = input('Ingrese descripción nueva asignatura: ')

    if cod_asignatura and nombre_asignatura != '':
        consulta = '''
            INSERT INTO asignaturas 
            (codigo_asig,nombre_asig,descripcion_asig,habilitado) 
            VALUES (%s,%s,%s,%s)
        '''
        valores = (cod_asignatura.upper(),
                   nombre_asignatura.title(), desc_asignatura, 1)
        mensaje = insertar_datos(consulta, valores)
        print(f'{mensaje}')
    else:
        print('El código y el nombre de la asignatura son campos obligatorios.')

# UPDATE DATA


def actualizar_asignatura():
    obtener_listado_asignaturas()
    busqueda = input("Ingrese asignatura a buscar: ")
    indice_asignatura = obtener_indice_data('asignaturas.py', busqueda)

    if indice_asignatura is not None:
        asignatura_modificada = input("Ingrese nuevo nombre de asignatura: ")
        asignaturas[indice_asignatura] = asignatura_modificada.title()
        mensaje = guardar_data('asignaturas', asignaturas, 'asignaturas.py')
        print(f'{mensaje} de asignatura {asignatura_modificada}')
    else:
        print('Asignatura NO encontrada')

# DELETE DATA


def eliminar_asignatura():
    obtener_listado_asignaturas()
    busqueda = input("Ingrese asignatura a buscar: ")
    indice_asignatura = obtener_indice_data('asignaturas.py', busqueda)

    if indice_asignatura is not None:
        asignatura = asignaturas[indice_asignatura]
        asignaturas.pop(indice_asignatura)
        mensaje = guardar_data('asignaturas', asignaturas, 'asignaturas.py')
        print(f'{mensaje}, asignatura {asignatura} eliminada.')
    else:
        print('Asignatura NO encontrada')
