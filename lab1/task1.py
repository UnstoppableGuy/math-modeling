from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo, showerror
import math
import random



def generate_data(count: float):
    return [random.random() <= count for _ in range(10**6)]


def is_valid(text):
    prob = 0
    try:
        prob = float(text)
    except:
        showerror(title="Info", message="Ошибка")
    finally:
        return prob


def show_result():
    value = field_entry.get()
    value = is_valid(text=value)
    random_values = generate_data(count=value)
    practical_probability = random_values.count(True) / len(random_values)
    showinfo(title="result", message='user - {0}\npractical - {1}'.format(value, practical_probability))


window = Tk()
window.title("Задание 1")
window.geometry("250x250")
field = DoubleVar()
field_entry = ttk.Entry(textvariable=field,justify=CENTER)
field_entry.pack(padx=5, pady=5)
btn = ttk.Button(text="Enter", command=show_result )
btn.pack()
window.mainloop()
