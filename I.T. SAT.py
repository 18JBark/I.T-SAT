
from tkinter import *

class Inventory_System:
    def __init__(self, master):
        self.master = master
        master.title("Inventory System")

        self.user = StringVar()
        self.user = Label(master, text="Username:")
        self.user.pack()

        self.passw = StringVar()
        self.passw = Label(master, text="Password:")
        self.passw.pack()

        self.login_button = Button(master, text="Login", command=master.login)
        self.login_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def Login(self, name):
        users = open ("usernames.txt",'r')
        for line in users:
            if name in line:
                for line in users:
                    if name in line:
                        print(line)


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
        file.write(' ')
        file.write(quantity)
        file.write(' ')
        file.write(description)
        file.write('\n')
        return


root = Tk()
my_gui = Inventory_ System(root)
root.mainloop()