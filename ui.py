import tkinter as tk
from tkinter import ttk

class WinAccess(tk.Tk):
    def __init__(self, userBd):
        super().__init__()
        self.title('SJE Docs')
        self.userBd = userBd
        self.status = bool()

        # Main Container
        frame = tk.LabelFrame(self, text = ' Control de Acceso ')
        frame.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        # User Input
        tk.Label(frame, text = ' Usuario: ').grid(row = 0, column = 0, sticky = tk.E)
        self.userInput = tk.Entry(frame, width = 16)
        self.userInput.focus()
        self.userInput.grid(row = 0, column = 1, pady = 5, sticky = tk.W)

        # Password Input
        tk.Label(frame, text = ' Contraseña: ').grid(row = 1, column = 0, sticky = tk.E)
        self.userPass = tk.Entry(frame, width = 16, show = '*')
        self.userPass.grid(row = 1, column = 1, pady = 5, sticky = tk.W)

        # Button Acept & Cancel
        self.statusButtAcept = False
        tk.Button(frame, text = 'Aceptar', command = lambda: self.getButtonAcept(frame)).grid(row = 3, column = 2, padx = 5, pady = 5)
        tk.Button(frame, text = 'Cancelar', command = self.destroy).grid(row = 3, column = 3, padx = 5, pady = 5)
    
    def getButtonAcept(self, frame):
        if self.userInput.get() == self.userBd[0] and self.userPass.get() == self.userBd[1]:
            self.destroy()
            self.status = True
        else:
            tk.Label(frame, text = 'Ingrese un usuario y contraseña válidos', fg = 'red').grid(row = 2, column = 1, sticky = tk.W)
            self.status = False

    def getStatus(self):
        return self.status

class WinForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('SJE Docs')
        self.geometry("800x600")
        self.resizable(False, False)

        # Main Container
        frame = tk.LabelFrame(self, text = 'Lista de documentos')
        frame.grid(row = 0, column = 0, padx = 10, pady = 10)

        # Doc selector, create, search
        self.docName = tk.StringVar()
        self.docOptions = ("Forma No 5", "Forma No 6", "Doc 3")
        tk.Label(frame, text = 'Seleccione un documento').grid(row = 0, column = 0, padx = 5, pady = 10)
        self.docChosen = ttk.Combobox(frame, width = 16, values = self.docOptions)
        self.docChosen.grid(row = 1, column = 0, padx = 5, pady = 5)

        # Button create, search
        tk.Button(frame, text = 'Crear  ').grid(row = 1, column = 1, padx = 3, pady = 3)
        tk.Button(frame, text = 'Buscar').grid(row = 1, column = 2, padx = 3, pady = 3)

