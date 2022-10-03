import math

from tkinter import ttk

from tkinter import *

from tkinter.messagebox import showinfo, showerror
import random


def generate_data(values):
    data = []
    for _ in range(10**6):
        value, prob_sum = random.random(), 0
        for event, probability in enumerate(values):
            prob_sum += probability
            if value <= prob_sum:
                data.append(event)
                break
    return data


def is_valid(text) -> float:
    prob = 0
    try:
        prob = float(text)
    except:
        showerror(title="Info", message="Ошибка")
    finally:
        return prob


def convert_string(text: str) -> list:
    values_str = text.split(" ")
    values_float = []
    for item in values_str:
        values_float.append(is_valid(item))
    eps = 1e-7
    if not (1 - eps <= sum(values_float) <= 1 + eps):
        showerror(message='Сумма не равна 1')
    else:    
        return values_float


def show_result():
    values = convert_string(field_entry.get())
    data = generate_data(values)
    for i, item in enumerate(sorted(set(data))):
        showinfo(title='result', message='Для {1} вероятности\nФактически:{0}'.format(
            data.count(item)/10**6, i+1))


window = Tk()
window.title("Задание 4")
window.geometry("250x250")
field = StringVar()
field_entry = ttk.Entry(textvariable=field, justify=CENTER)
field_entry.pack(padx=5, pady=5)
btn = ttk.Button(text="Enter", command=show_result)
btn.pack()
window.mainloop()
