
from tkinter import ttk
from tkinter import *

import sqlite3

class nomina:

    def __init__(self,window): 
        self.wind = window
        self.wind.title('Nomina generate')

if __name__ == '__main__':
    window = Tk()
    application = nomina(window)
    window.mainloop()

