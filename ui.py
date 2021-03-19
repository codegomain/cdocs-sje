import tkinter as tk

class WinAccess(tk.Tk):
    def __init__(self, userBd):
        super().__init__()
        self.title('SJE Docs')
        self.userBd = userBd

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
        tk.Button(frame, text = 'Cancelar', command = self.quit).grid(row = 3, column = 3, padx = 5, pady = 5)
    
    def getButtonAcept(self, frame):
        if self.userInput.get() == self.userBd[0] and self.userPass.get() == self.userBd[1]:
            self.quit()
        else:
            tk.Label(frame, text = 'Ingrese un usuario y contraseña validos', fg = 'red').grid(row = 2, column = 1, sticky = tk.W)



