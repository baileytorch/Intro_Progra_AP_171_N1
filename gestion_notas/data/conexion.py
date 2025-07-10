import mysql.connector
from mysql.connector import errorcode
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
            print('No se ha podido establecer conexión con la base de datos')
    except mysql.connector.Error as error_conexion:
        if error_conexion.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Credenciales de acceso incorrectas')
        elif error_conexion.errno == errorcode.ER_BAD_DB_ERROR:
            print('Base de datos incorrecta o no existe')
        else:
            print(error_conexion)
    else:
        conexion.close()


def leer_datos(consulta):
    conexion = conectar_db()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        if cursor != None:
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        else:
            print("Su búsqueda no arrojó resultados...")
        conexion.close()


def insertar_datos(consulta, datos):
    conexion = conectar_db()
    if conexion and conexion.is_connected():
        cursor = conexion.cursor()
        if cursor != None:
            cursor.execute(consulta, datos)
            conexion.commit()
            id = cursor.lastrowid
            cursor.close()
            return print(f"Id registro insertado = {id}")
        else:
            print("Su búsqueda no arrojó resultados...")
        conexion.close()
