
from tkinter import ttk
from tkinter import *

import sqlite3

class nomina:

    db_name = 'database.db'

    def __init__(self,window): 
        self.wind = window
        self.wind.title('Nomina generate')

        #crear contenedor
        frame = LabelFrame(self.wind, text = 'register a new nomina')
        frame.grid(row = 0, column= 0, columnspan= 3, pady=20)

        #name input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column= 1)

        #salary input
        Label(frame, text='Salary: ').grid(row= 2, column= 0)
        self.salary = Entry(frame)
        self.salary.grid(row=2, column=1)

        #days input
        Label(frame, text='Days worked: ').grid(row= 3, column= 0)
        self.days = Entry(frame)
        self.days.grid(row=3, column=1)

        #add button
        ttk.Button(frame, text = 'Generate nomina').grid(row=4,columnspan=2, sticky= W + E)

        #table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=5, column=0, columnspan= 2)
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1',text='Salary', anchor=CENTER)

        self.get_nomina()

    def run_query(self, query,parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_nomina(self):
        
        #delet records
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #consulta    

        query = 'SELECT * FROM Nomina ORDER BY Name DESC'       
        db_rows=self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])



if __name__ == '__main__':
    window = Tk()
    application = nomina(window)
    window.mainloop()

