from data.crear_data import guardar_data
from data.leer_data import listado_data, obtener_indice_data
from data.asignaturas import asignaturas
from data.conexion import buscar_dato, leer_datos, insertar_actualizar_datos
from prettytable import PrettyTable

# READ DATA


def obtener_listado_asignaturas():
    print()
    print('Listado de Asignaturas')
    print('======================')
    consulta = f'''
        SELECT id_asignatura,codigo_asig,nombre_asig,descripcion_asig
        FROM asignaturas
        WHERE habilitado = 1
    '''
    tabla_asignaturas = PrettyTable()
    tabla_asignaturas.field_names = [
        'N°', 'Código Asignatura', 'Nombre Asignatura', 'Descripción Asignatura']
    listado_asignaturas = leer_datos(consulta)
    if listado_asignaturas != None:
        for asignatura in listado_asignaturas:
            tabla_asignaturas.add_row(asignatura)  # type: ignore
    else:
        print('No se han encontrado datos.')
    print(tabla_asignaturas)


def obtener_asignatura_codigo(cod):
    consulta = '''
        SELECT codigo_asig,nombre_asig,descripcion_asig
        FROM asignaturas
        WHERE codigo_asig = %s AND habilitado = %s
    '''
    parametros = (cod, 1)
    asignatura = leer_datos(consulta, parametros)
    if asignatura != None:
        return asignatura
    else:
        print('No se ha encontrado la asignatura.')


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
        parametros = (
            cod_asignatura.upper(),
            nombre_asignatura.title(),
            desc_asignatura,
            1)
        mensaje = insertar_actualizar_datos(consulta, parametros)
        print(f'{mensaje}')
    else:
        print('El código y el nombre de la asignatura son campos obligatorios.')

# UPDATE DATA


def actualizar_asignatura():
    obtener_listado_asignaturas()
    lista_id = []
    id_asig = 0
    codigo_asignatura = ''
    nombre_asignatura = ''
    descripcion_asignatura = ''
    tabla_asignatura = PrettyTable()
    tabla_asignatura.field_names = [
        'N°', 'Código Asignatura', 'Nombre Asignatura', 'Descripción Asignatura']

    id_asignatura = input(
        'Ingrese el N° de la asignatura que desea modificar: ')
    if id_asignatura != '':
        try:
            id_asig = int(id_asignatura)
            lista_id.append(id_asig)
            consulta = '''
                SELECT id_asignatura,codigo_asig,nombre_asig,descripcion_asig
                FROM asignaturas
                WHERE habilitado = 1
                AND id_asignatura = %s
            '''
            asignatura = buscar_dato(consulta, lista_id)
            if asignatura != None:
                for data in asignatura:  # type: ignore
                    codigo_asignatura = data[1]  # type: ignore
                    nombre_asignatura = data[2]  # type: ignore
                    descripcion_asignatura = data[3]  # type: ignore
                tabla_asignatura.add_row(asignatura[0])  # type: ignore
            print(tabla_asignatura)
        except ValueError:
            print('Ingrese un N° de asignatura válido.')

    cod_asig_usuario = input(
        "Ingrese CÓDIGO de asignatura, o ENTER para conservar: ")
    nom_asig_usuario = input(
        'Ingrese nombre asignatura, o ENTER para conservar: ')
    desc_asig_usuario = input(
        'Ingrese descripción asignatura, o ENTER para conservar: ')

    if cod_asig_usuario != '':
        codigo_asignatura = cod_asig_usuario.upper()
    if nom_asig_usuario != '':
        nombre_asignatura = nom_asig_usuario.title()
    if desc_asig_usuario != '':
        descripcion_asignatura = desc_asig_usuario
    consulta = '''
        UPDATE asignaturas SET 
            codigo_asig = %s,
            nombre_asig = %s,
            descripcion_asig = %s,
            habilitado = %s
        WHERE id_asignatura = %s
    '''
    parametros = (
        codigo_asignatura,
        nombre_asignatura,
        descripcion_asignatura,
        1,
        id_asig)
    mensaje = insertar_actualizar_datos(consulta, parametros)
    print(f'{mensaje}')

# DELETE DATA


def eliminar_asignatura():
    obtener_listado_asignaturas()
    lista_id = []
    id_asig = 0

    id_asignatura = input(
        'Ingrese el N° de la asignatura que desea modificar: ')
    if id_asignatura != '':
        try:
            id_asig = int(id_asignatura)
            lista_id.append(id_asig)
            consulta = '''
                SELECT id_asignatura
                FROM asignaturas
                WHERE id_asignatura = %s
            '''
            asignatura = buscar_dato(consulta, lista_id)
            if asignatura != None:
                for data in asignatura:  # type: ignore
                    id_asig = data[0]  # type: ignore
        except ValueError:
            print('Ingrese un N° de asignatura válido.')

    consulta = '''
        UPDATE asignaturas SET
            habilitado = %s
        WHERE id_asignatura = %s
    '''
    parametros = (
        0,
        id_asig)
    mensaje = insertar_actualizar_datos(consulta, parametros)
    print(f'{mensaje}')
