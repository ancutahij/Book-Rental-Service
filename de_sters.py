"""from tkinter import Tk, Label, Button

from ui.book_console import BookConsole


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        #self.greet_button = Button(master, text="Greet", command=BookConsole([]))
        #self.greet_button.pack()
        file = Menu(menu)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
"""
"""
import tkinter as tk

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("To-Do App v1")
        self.geometry("300x400")

        todo1 = tk.Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black",
        pady=10)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.task_create = tk.Text(self, height=3, bg="white", fg="black")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        self.bind("<Return>", self.add_task)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": " white"}]

        def add_task(self, event=None):
            task_text = self.task_create.get(1.0,tk.END).strip()

            if len(task_text) > 0:
                new_task = tk.Label(self, text=task_text, pady=10)

            _, task_style_choice = divmod(len(self.tasks), 2)

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])

            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

            self.task_create.delete(1.0, tk.END)

if __name__ == "__main__":
t  todo = Todo()
    todo.mainloop()

import sys
import py
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
"""





def verifMultime(l):
    for i in range(0, len(l)-1):
        for j in range (i+1, len(l)):
            if l[i]==l[j]:
                return False
    return True

def test_verifMultime():
    l=[2,3,2,4]
    assert verifMultime(l)==False
    """
        Caz fav:
         -primele 2 sunt egale: T(n)=1( nr de comparari, apartine lui Teta)
        Caz defav:
         - este multime: T(n)=  n^2
         
         tabele de dispersie??
    """

test_verifMultime()

def sumaPare(l):
    """
        Caz fav: nu exista
        Caz defav: nu exista

        T(n)=    1+T(n/2) + T(n/2)
                 1, n

        T(n) = 1+2T(n/2)
        n= 2^k
        T(2^k) = 1+2T(2^(k-1))
        T(2^(k-1) =1 + 2T(2^(k-2))
        ...
        T(2)= 1 +2 T(n^0)
    """
    if len(l)== 0 :
        return 0
    if len(l)==1:
        if l[0]%2==0:
            return l[0]
        else:
            return 0
    m=len(l)//2
    return sumaPare(l[:m])+sumaPare(l[m:])











