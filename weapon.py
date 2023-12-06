from tkinter import Tk, Canvas, ARC, W
 
 
class Weapon():
    def __init__(self,canvas,damage):
        self._canvas=c
        self._baseDamage=d
        self._name=n
        
    def display(self, x, y):
        pass
    
    def hit(self):
        damage=randrange(sel._baseDamage-5, self._baseDamage+5)
        print(damage)
        return damage