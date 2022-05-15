import tkinter as tk


class principal():

    def __init__(self):
        self.principal = tk.Tk()
        self.pantallaPrincipal()
        self.principal.mainloop()

    
    def pantallaPrincipal(self):
        #labels
        self.Administrar_clientes = tk.Label(self.principal, text='Administrar_clientes: ')
        self.Administrar_clientes.config(font=('Arial','20','bold'))
        self.Administrar_clientes.grid(row=1,column=0,padx=10,pady=10)
        self.Administrar_pedidos = tk.Label(self.principal, text='Administrar_pedidos: ')
        self.Administrar_pedidos.config(font=('Arial','12','bold'))
        self.Administrar_pedidos.grid(row=2,column=0,padx=10,pady=10)
        self.Almacen = tk.Label(self.principal, text='Almacen: ')
        self.Almacen.config(font=('Arial','12','bold'))
        self.Almacen.grid(row=3,column=0,padx=10,pady=10)

        #botones
        self.botonAdminClientes = tk.Button(self.principal,text="Administrar_clientes")
        self.botonAdminClientes.config(font=('Arial','20','bold'))
        self.botonAdminClientes.grid(row=1,column=1,padx=10,pady=10)
        self.botonAdminClientes = tk.Button(self.principal,text="Administrar_pedidos")
        self.botonAdminClientes.config(font=('Arial','20','bold'))
        self.botonAdminClientes.grid(row=2,column=1,padx=10,pady=10)
        self.botonAdminClientes = tk.Button(self.principal,text="Almacen")
        self.botonAdminClientes.config(font=('Arial','20','bold'))
        self.botonAdminClientes.grid(row=3,column=1,padx=10,pady=10)

