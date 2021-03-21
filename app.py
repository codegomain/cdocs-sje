from ui import WinAccess, WinForm

def main():
    userBd = ('Diego', 'qwerty')
    winpass = WinAccess(userBd)
    winpass.mainloop()
    if winpass.getStatus() == True:
        windocs = WinForm()
        windocs.mainloop()
    else:
        print('salir')

if __name__ == "__main__":
    main()