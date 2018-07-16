
from tkinter import *


class LoginScreen:
    def __init__(self, master):
        self.master = master
        master.title("Inventory System")

        self.usern = StringVar()
        self.usern = Label(master, text="Username:")
        self.usern.pack()
        self.usern.grid(row=1, column=0)

        self.user = StringVar()
        self.user = Entry(master)
        self.user.pack()
        self.user.grid(row=1, column=1)

        self.passwo = StringVar()
        self.passwo = Label(master, text="Password:")
        self.passwo.pack()
        self.passwo.grid(row=2, column=0)

        self.passw = StringVar()
        self.passw = Entry(master)
        self.passw.pack()
        self.passwo.grid(row=2, column=1)

        self.login_button = Button(master, text="Login", command=self.Login)
        self.login_button.pack()
        self.login_button.grid(row=3, column=0)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        self.close_button.grid(row=3, column=1)

    def Login(self, user, passw):
        users = open ("usernames.txt",'r')
        for line in users:
            if user in line:
                for line in users:
                    if passw in line:
                        self.CreateMainScreen()

    def CreateMainScreen(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Main = MainScreen(self.newWindow)



class MainScreen:
    def __init__(self, master):
        self.master = master
        master.title("Inventory System")

        self.search = StringVar()
        self.search = Label(master, text="Search:")
        self.search.pack()

        self.SearchFunc = StringVar()
        self.SearchFunc = Entry(master, option='search')
        self.SearchFunc.pack()

        self.Search_button = Button(master, text="Search", command=self.SearchFunction())
        self.Search_button.pack()

        self.Stock_button = Button(master, text="Stock", command=self.Stock())
        self.Stock_button.pack()

        self.Logout_button = Button(master, text="Logout", command=self.CreateLoginScreen())
        self.Logout_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


    def CreateLoginScreen(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Log = LoginScreen(self.newWindow)

    def CreateSearchScreen(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Log = SearchScreen(self.newWindow)

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


class SearchScreen:
    def __init__(self, master):
        self.master = master
        master.title("Inventory System")


class InfoScreen:
    def __init__(self, master):
        self.master = master
        master.title("Inventory System")


root = Tk()
my_gui = LoginScreen(root)
root.mainloop()