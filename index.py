
from ast import Delete
from tkinter import ttk
from tkinter import *

import sqlite3
from unicodedata import name

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
        ttk.Button(frame, text = 'Generate nomina', command= self.add_nomina).grid(row=5,columnspan=2, sticky= W + E)

        # output messages
        self.message = Label(text='', fg='blue')
        self.message.grid(row=4, column=0, columnspan=2, sticky= W + E)

        #table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=6, column=0, columnspan= 2)
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1',text='Salary', anchor=CENTER)

        #buttons
        ttk.Button(text= 'DELETE', command= self.delete_nomina).grid(row=7, column= 0, sticky= W+E)
        ttk.Button(text= 'EDIT', command= self.edit_nomina).grid(row=7, column= 1, sticky= W+E)

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

    def validation(self):
        return len(self.name.get()) !=0 and len(self.salary.get()) !=0

    def add_nomina(self): 
        if self.validation():
            query='INSERT INTO Nomina VALUES(NULL,?,?)'
            parameters =(self.name.get(), self.salary.get())
            self.run_query(query,parameters)
            self.message['text'] = 'Nomina of {} added Successfully'.format(self.name.get())
            self.name.delete(0,END)
            self.salary.delete(0,END)
            self.days.delete(0,END)
         
        else:
            self.message['text'] = 'Name and Salary is required'
        self.get_nomina() 

    def delete_nomina(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a record'
            return
        self.message['text'] = ''    
        name= self.tree.item(self.tree.selection())['text']    
        query = 'DELETE FROM Nomina WHERE Name = ?'   
        self.run_query(query, (name, )) 
        self.message['text'] = 'Record of {} deleted successfully'.format(name)

    def edit_nomina(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a record'
            return   
        name = self.tree.item(self.tree.selection()) ['text']
        old_salary= self.tree.item(self.tree.selection()) ['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title('Edit Nomina')        







if __name__ == '__main__':
    window = Tk()
    application = nomina(window)
    window.mainloop()

