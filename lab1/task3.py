import math

from tkinter import ttk

from tkinter import *

from tkinter.messagebox import showinfo, showerror
import random


def generate_data(count: float):

    return [random.random() <= count for _ in range(10**6)]


def is_valid(text) -> float:

    prob = 0

    try:

        prob = float(text)

    except:

        showerror(title="Info", message="Ошибка")

    finally:
        return prob


def set_data(a_value, b_value):
    data = list()
    for _ in range(10**6):
        if_A = random.random() <= a_value
        if if_A:
            if_B = random.random() <= b_value
        else:
            if_B = random.random() <= 1 - b_value

        if if_A and if_B:
            res = 0
        elif if_A and not if_B:
            res = 1
        elif not if_A and if_B:
            res = 2
        elif not if_A and not if_B:
            res = 3
        data.append(res)
    return data


def math_values(data):
    strings = []
    for i, item in enumerate(sorted(set(data))):
        strings.append(
            f'Actual {item} events:\npractical - {data.count(item) / 10**6}')
    return strings


def theoretical_values(A, B):
    data = []
    data.append(f'P(AB) = {A * B}')
    data.append(f'P(AB¯) = {A * (1-B)}')
    data.append(f'P(A¯B) = {(1-A) * (1-B)}')
    data.append(f'P(A¯B¯) = {(1-A) * (1-(1-B))}')

    return data


def show_result():
    A = is_valid(field_a_entry.get())
    B = is_valid(field_b_entry.get())
    data = set_data(A, B)
    string_t = theoretical_values(A, B)
    strings_c = math_values(data)
    for i in range(len(string_t)):
        showinfo(title="result",
                 message='{1}\ntheoretical - \n{0}'.format(string_t[i], strings_c[i]))


window = Tk()

window.title("Задание 3")

window.geometry("250x250")


field_a = StringVar()

field_a.set("Вероятность А")

field_b = StringVar()

field_b.set("Вероятность B|A")


field_a_entry = ttk.Entry(textvariable=field_a, justify=CENTER)

field_a_entry.pack(padx=5, pady=5)

field_b_entry = ttk.Entry(textvariable=field_b, justify=CENTER)

field_b_entry.pack(padx=5, pady=5)


btn = ttk.Button(text="Enter", command=show_result)

btn.pack()

window.mainloop()
