<<<<<<< HEAD
import tkinter as tk
#from client.gui_app import *

def main():
    root = tk.Tk() #raiz
    root.title('Loggin Cliente')
    root.mainloop()

if __name__ == '__main__':
    main()
=======
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
        
>>>>>>> 98aea1ec019ff7e2461a2bbc70e8e019dd98d10f
