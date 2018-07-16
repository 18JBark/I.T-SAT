
from tkinter import *


class LoginScreen:
    def __init__(self, master):
        self.master = master
        master.title("Inventory System")

        self.usern = StringVar()
        self.usern = Label(master, text="Username:")
        self.usern.pack()

        self.user = StringVar()
        self.user = Entry(master, option='name')
        self.user.pack()

        self.passwo = StringVar()
        self.passwo = Label(master, text="Password:")
        self.passwo.pack()

        self.passw = StringVar()
        self.passw = Entry(master, option='pass')
        self.passw.pack()

        self.login_button = Button(master, text="Login", command=self.Login)
        self.login_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def Login(self, name):
        users = open ("usernames.txt",'r')
        for line in users:
            if name in line:
                for line in users:
                    if name in line:
                        self.CreateWindow()

    def CreateWindow(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Main = MainScreen(self.newWindow)

    def SearchFunction(name, self):
        print('Search function')
        with open("stock.txt") as f:
            for line in f:
                if name in line:
                    print(line)
        return


    def Stock(self):
        file = open ("stock.txt",'a')
        item = input('Enter a name: ')
        quantity = input('Enter quantity: ')
        description = input('Enter description: ')
        file.write(item)
        file.write(', ')
        file.write(quantity)
        file.write(', ')
        file.write(description)
        file.write('\n')
        return

class MainScreen:
    def __init__(self, master):

root = Tk()
#my_gui = Inventory_System(root)
root.mainloop()