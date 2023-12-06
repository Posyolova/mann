from tkinter import Tk, Canvas, ARC
from weapon import Weapon
from random import randrange


class Shield(Weapon):

    def __init__(self, c, d, n):
        self._canvas = c
        self._baseDamage = d
        self._name = n

    def display(self, x, y):
        self._canvas.create_arc(x-2,y+120,x+60,y-170, start=180, extent=180,style=ARC, fill="grey", width=3)
        

