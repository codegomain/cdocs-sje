from ui import WinAccess

def main():
    userBd = ('Diego', 'qwerty')
    winpass = WinAccess(userBd)
    winpass.mainloop()

if __name__ == "__main__":
    main()