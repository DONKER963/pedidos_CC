import mysql.connector

class DB:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root',
            password ='',
            host = 'localhost',
            database = 'base_datos'
        )
        #print('conexion')
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.close()