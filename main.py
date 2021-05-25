from tkinter import *
import time
import datetime
import random


root = Tk()
root.title("Sistema de Vendas BD Group")
root.geometry('1350x750+0+0')


class Principal:
    def __init__(self,master,*args, **kwargs):
        self.master = master
        
        self.left = Frame(master, width = 700, height = 768, bg = 'white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width = 700, height = 768, bg = 'white')
        self.right.pack(side=LEFT)


b = Principal(root)
root.mainloop()