import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    database='gestion_notas'
)

cursor = conexion.cursor()

cursor.execute('SELECT * FROM asignaturas')
resultado = cursor.fetchall()
print(resultado)