from tkinter import *
import tkinter
import tkinter.messagebox
import sqlalchemy
import pandas as pd
from datetime import datetime

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