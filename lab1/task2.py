import math
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo, showerror
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


def split_string(text: str) -> list:
    values_str = text.split(" ")
    values_float = [float(item) for item in values_str]
    return values_float


def show_result():
    text = field_entry.get()
    values_f = split_string(text)
    list_in = [generate_data(item) for item in values_f]
    res = [sum((list(item)))/(10**6) for item in list_in]
    showinfo(title="result",
             message='user - {0}\npractical - {1}'.format(values_f, res))

window = Tk()
window.title("Задание 2")
window.geometry("250x250")

field = StringVar()
field_entry = ttk.Entry(textvariable=field, justify=CENTER)
field_entry.pack(padx=5, pady=5)

btn = ttk.Button(text="Enter", command=show_result)
btn.pack()

window.mainloop()
