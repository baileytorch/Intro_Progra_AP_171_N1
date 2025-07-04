import mysql.connector
from mysql.connector import errorcode
from auxiliares.data_conexion import servidor,puerto,usuario,base_datos,contrasena

def conectar_db(consulta):
    try:
        conexion = mysql.connector.connect(
            host = servidor,
            port = puerto,
            user = usuario,
            database = base_datos,
            password = contrasena
        )

        if conexion  and conexion.is_connected():
            cursor = conexion.cursor()

            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        else:
            print('No se ha podido establecer conexión con la base de datos')
    except mysql.connector.Error as error_conexion:
        if error_conexion.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Credenciales de acceso incorrectas')
        elif error_conexion.errno == errorcode.ER_BAD_DB_ERROR:
            print('Base de datos incorrecta o no existe')
        else:
            print(error_conexion)