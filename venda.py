from tkinter import *
import tkinter
import tkinter.messagebox
import sqlalchemy
import pandas as pd
from datetime import date

root = Tk()
root.title("Produtos")
root.geometry('1350x750+0+0')


server =  '127.0.0.1'
database = 'OPE'
username = 'sa'
password = '9970568'
driver = 'ODBC Driver 17 for SQL Server'
database_con = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"

engine = sqlalchemy.create_engine(database_con)
con = engine.connect()

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')
class Vendas:
    def __init__(self,master,*args, **kwargs):
        self.master = master
        
        self.left = Frame(master, width = 700, height = 768, bg = 'lightgrey')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width = 700, height = 768, bg = 'white')
        self.right.pack(side=RIGHT)

        self.cabecalho = Label(self.left, text="Vendas: ", font=("arial 40 bold"), bg = 'lightgrey')
        self.cabecalho.place(x=0,y=0)

        self.hora = Label(self.right, text="Data: " + data_em_texto , font=("arial 40 bold"), bg = 'white')
        self.hora.place(x=0,y=0)




b = Vendas(root)
root.mainloop()