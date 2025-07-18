import mysql.connector
from mysql.connector import Error, errorcode
from auxiliares.data_conexion import servidor, puerto, usuario, base_datos, contrasena


def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host=servidor,
            port=puerto,
            user=usuario,
            database=base_datos,
            password=contrasena
        )

        if conexion and conexion.is_connected():
            return conexion
        else:
            print('Error: No se ha podido establecer conexión con la base de datos')
    except mysql.connector.Error as error_conexion:
        if error_conexion.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Error: Credenciales de acceso incorrectas')
        elif error_conexion.errno == errorcode.ER_BAD_DB_ERROR:
            print('Error: Base de datos incorrecta o no existe')
        elif error_conexion.errno == errorcode.CR_CONN_HOST_ERROR:
            print('Error: No es posible conectarse a la base de datos especificada.')
        else:
            print(f'Error: {error_conexion}')
    else:
        conexion.close()


def buscar_dato(consulta, datos=None):
    conexion = conectar_db()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        resultado = None
        if cursor != None:
            if datos != '' and datos != None:
                cursor.execute(consulta, datos)
                resultado = cursor.fetchall()
                cursor.close()
            else:
                cursor.execute(consulta)
                resultado = cursor.fetchone()
                cursor.close()
            return resultado
        else:
            print("Su búsqueda no arrojó resultados...")
        conexion.close()


def leer_datos(consulta, datos=None):
    conexion = conectar_db()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        resultado = None
        if cursor != None:
            if datos != '' and datos != None:
                cursor.execute(consulta, datos)
                resultado = cursor.fetchall()
                cursor.close()
            else:
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                cursor.close()
            return resultado
        else:
            print("Su búsqueda no arrojó resultados...")
        conexion.close()


def insertar_actualizar_datos(consulta, datos):
    conexion = conectar_db()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        if cursor != None:
            try:
                cursor.execute(consulta, datos)
                conexion.commit()
                if cursor.lastrowid:
                    id = cursor.lastrowid
                    return print(f"Id registro insertado = {id}")
            except Error as error_ejecucion:
                conexion.rollback()
                print(f'Error: {error_ejecucion.msg}')
            finally:
                cursor.close()
                conexion.close()
        else:
            print("Su búsqueda no arrojó resultados...")
