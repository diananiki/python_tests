from tkinter import *
from playsound import playsound
import random


def func():
    playsound('urr-cute.mp3')
    n = int(var_val.get())
    arr = [i for i in stud_val.get().split(' ')]
    var_lb.destroy()
    stud_lb.destroy()
    var_val.destroy()
    stud_val.destroy()
    btn.destroy()
    for i in range(len(arr)):
        lb = Label(frame, text=arr[i] + '-' + str(random.randint(1, n)), font=("Courier New", 16), bg="pink")
        lb.grid(row=i + 1, column=1)


window = Tk()
window.title("Распределение вариантов")
window.geometry('550x300')
frame = Frame(window, padx=10, pady=10, bg="pink")
frame.pack(expand=True)
var_lb = Label(frame, text="Введите количество вариантов ", font=("Courier New", 16), bg="pink")
var_lb.grid(row=1, column=1)
var_val = Entry(frame)
var_val.grid(row=1, column=2)
stud_lb = Label(frame, text="Введите список учеников ", font=("Courier New", 16), bg="pink")
stud_lb.grid(row=2, column=1)
stud_val = Entry(frame)
stud_val.grid(row=2, column=2)
btn = Button(frame, text="Распределить", font=("Courier New", 18), command=func, bg="skyblue", relief="raised")
btn.grid(row=5, column=1)
window.mainloop()