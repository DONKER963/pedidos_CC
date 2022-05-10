import tkinter as tk
from model.loggin import *
from client.principal import *

class loggin(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root,width=600,height=500)
        #ventana
        self.root = root
        self.pack()

        self.pantallaLogin()
    

    def pantallaLogin(self):
        #etiqueta ID
        self.label_ID = tk.Label(self, text='ID: ')
        self.label_ID.config(font=('Arial','12','bold'))
        self.label_ID.grid(row=0,column=0,padx=10,pady=10)
        #etiqueta contraseña
        self.label_pass = tk.Label(self,text='Contraseña: ')
        self.label_pass.config(font=('Arial','12','bold'))
        self.label_pass.grid(row=1,column=0,padx=10,pady=10)
        #--entry
        #cajatexto ID
        self.ID = tk.StringVar()
        self.entry_ID = tk.Entry(self,textvariable=self.ID)
        self.entry_ID.config(width=30)
        self.entry_ID.grid(row=0,column=1,padx=10,pady=10)
        #cajatexto contraseña
        self.password = tk.StringVar()
        self.entry_pass = tk.Entry(self, textvariable=self.password)
        self.entry_pass.config(width=30,show='*')
        self.entry_pass.grid(row=1,column=1,padx=10,pady=10)


        #boton ingresar
        self.ingresar = tk.Button(self,text="INGRESAR",command=self.verificaDatos)#creacion
        #self.ingresar.config()#cuando puchas el boton
        self.ingresar.grid(row=2,column=0,padx=10,pady=10,columnspan=2)#acomodarlo
        
    #funcinoes
    def verificaDatos(self):
        x = ver_log(
            self.ID.get(),#variable NO CAJA DE TEXTO
            self.password.get()#variable NO CAJA TEXTO
        )
        self.ID.set('')
        self.password.set('')
        
        if x:
            self.root.destroy()
            principal()






def main():
    root = tk.Tk() #raiz
    app = loggin(root = root)
    app.mainloop()

if __name__ == '__main__':
    main()