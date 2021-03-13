import tkinter as tk

class WinAccess(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('SJE Docs')

        # Main Container
        frame = tk.LabelFrame(self, text = ' Control de Acceso ')
        frame.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        # User Input
        tk.Label(frame, text = ' Usuario: ').grid(row = 0, column = 0)
        self.userInput = tk.Entry(frame, width = 16)
        self.userInput.focus()
        self.userInput.grid(row = 0, column = 1, pady = 5)

        # Password Input
        tk.Label(frame, text = ' Contraseña: ').grid(row = 1, column = 0)
        self.userPass = tk.Entry(frame, width = 16, show = '*')
        self.userPass.grid(row = 1, column = 1, pady = 5)

        # Button Acept & Cancel
        tk.Button(frame, text = 'Aceptar').grid(row = 2, column = 2, padx = 5, pady = 5)
        tk.Button(frame, text = 'Cancelar').grid(row = 2, column = 3, padx = 5, pady = 5)