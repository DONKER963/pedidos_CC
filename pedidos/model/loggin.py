from .conexion import *
from tkinter import messagebox

def ver_log(id,password):
    conexion = DB()
    sql = f"SELECT * FROM usuarios WHERE ID = {id} AND contra = '{password}'"
    try:
        conexion.cursor.execute(sql)
    except:
        pass
    idx = conexion.cursor.fetchone()
    if idx:
        messagebox.showinfo(message='BIENVENIDO')
    else:
        messagebox.showwarning(message='usuario o contraseña erroneos')
    conexion.cursor.close()
    return idx