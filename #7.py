#3x+1

import time
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
numero = simpledialog.askinteger(title="3x+1 nummer", prompt="wuts je nummer:")

lst = []

#numero = int(input("3x+1 , "))
while numero != 1:
    if numero % 2 == 0:
        numero = numero / 2

    elif numero % 2 != 0:
        numero = numero * 3 + 1
    lst.append(numero)
     


y_pos = np.arange(len(lst))
performance = lst

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, lst)

plt.show()