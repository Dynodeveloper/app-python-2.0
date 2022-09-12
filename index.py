
from tkinter import ttk
from tkinter import *

import sqlite3

class nomina:

    def __init__(self,window): 
        self.wind = window
        self.wind.title('Nomina generate')

        #crear contenedor
        frame = LabelFrame(self.wind, text = 'register a new nomina')
        frame.grid(row = 0, column= 0, columnspan= 3, pady=20)

        #name input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column= 1)

        #salary input
        Label(frame, text='Salary: ').grid(row= 2, column= 0)
        self.salary = Entry(frame)
        self.salary.grid(row=2, column=1)

        #add button
        ttk.Button(frame, text = 'Generate nomina').grid(row=3,columnspan=2, sticky= W + E)


if __name__ == '__main__':
    window = Tk()
    application = nomina(window)
    window.mainloop()

