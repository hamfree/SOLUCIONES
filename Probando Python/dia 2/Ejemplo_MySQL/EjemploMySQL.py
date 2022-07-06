# lo primero que tenemos que hacer es descargar e instalar el conector conmySQL en nuestro equipo

# Importamos el conector de MySQL
import mysql.connector
 
# Variable con la configuracion de la conexion
config_mysql = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'prueba',
}
 
# conectamos al servidor MySql
conector = mysql.connector.connect(**config_mysql)
 
# cursor, clase para el manejo del SQL ???
cursor = conector.cursor()
 
# Creamos la consulta SQL
query = ("SELECT * FROM tabla1")
 
# Ejecutamos la consula SQL
cursor.execute(query)
 
# Mostramos todos los datos de la consulta
for (campo1, campo2) in cursor:
    print("Campo1: " + campo1 + ", Campo2: " + campo2)
 
# Cerramos cursor
cursor.close()
 
# Cerramos la conexion
conector.close()