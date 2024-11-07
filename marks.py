import sqlite3
import random
from tkinter import *
from tkinter import ttk

base = sqlite3.connect('student.db')
cur = base.cursor()
marks = [i for i in range(1, 21)]
weights = [1/48] * 14 + [1/8] * 6
for i in cur.execute('SELECT student FROM list').fetchall():
    cur.execute('UPDATE list SET task1 == ?, task2 == ?, task3 == ?, task4 == ?, task5 == ?, automate == ?'
                'WHERE student == ?', (*random.choices(marks, weights=weights, k=5), *random.choices([0, 1], weights=[0.8, 0.2]), i[0]))
base.commit()

window = Tk()
window.title("База данных 'Студенты'")
window.geometry('800x350')
students = cur.execute('SELECT * FROM list').fetchall()
columns = ['student', 'task1', 'task2', 'task3', 'task4', 'task5', 'automate', 'sum', 'mark']
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
for i in columns:
    tree.column(i, width=50)
    tree.heading(i, text=i)
tree.column('student', width=100)
for student in students:
    tree.insert("", END, values=student)
window.mainloop()