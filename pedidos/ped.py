#para conectar con mysql
import pymysql
#para mostrar mensajes
def tkinter import messagebox
def primeraconexion();
  try:
        miconexion = pymysql.connect(host="localhost", user="root", password="", db="mysql")
        micursor = miconexion.cursor()
        micursor.execute("CREATE DATABASE IF NOT EXIST empresa")
        miconexion.close()
        micursor.close()
        #creacion de la tabla
        
