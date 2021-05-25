from tkinter import *
import tkinter
import tkinter.messagebox
import sqlalchemy
import pandas as pd
from datetime import datetime

root = Tk()
root.title("Produtos")
root.geometry('870x555+0+0')


server =  '127.0.0.1'
database = 'OPE'
username = 'sa'
password = '9970568'
driver = 'ODBC Driver 17 for SQL Server'
database_con = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"

engine = sqlalchemy.create_engine(database_con)
con = engine.connect()


resultado = pd.read_sql_query("SELECT TOP 1 (IDPRODUTO) FROM PRODUTO ORDER BY IDPRODUTO DESC",con)
for r in resultado:
    IDPRODUTO=r[0]
class Cadastrar:
    def __init__(self,master,*args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Produtos", font=("arial 40 bold"), fg="black")
        self.heading.pack(anchor=CENTER)

        self.idproduto = Label(master, text="ID: ", font=("arial 18 bold"))
        self.idproduto.place(x=0,y=120)
        self.idproduto_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.idproduto_entrada.place(x=380,y=120)
        self.btn_pesquisarid = Button(master, text="Pesquisar", width=12, height=1, bg='orange', font=("arial 12 bold"), command= self.pesquisarid)
        self.btn_pesquisarid.place(x=720,y=120)

        self.nome_produto = Label(master, text="Nome Produto:", font=("arial 18 bold"))
        self.nome_produto.place(x=0,y=170)
        self.nome_produto_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.nome_produto_entrada.place(x=380,y=170)
        self.btn_pesquisarnome = Button(master, text="Pesquisar", width=12, height=1, bg='orange', font=("arial 12 bold"), command =self.pesquisarnome)
        self.btn_pesquisarnome.place(x=720,y=170)


        self.ativo= Label(master, text="Ativo: ", font=("arial 18 bold"))
        self.ativo.place(x=0,y=220)
        self.ativo_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.ativo_entrada.place(x=380,y=220)
        
        self.datacriado = Label(master, text="Data Criado: ", font=("arial 18 bold"))
        self.datacriado.place(x=0,y=270)
        self.datacriado_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.datacriado_entrada.place(x=380,y=270) 

        self.estoque= Label(master, text="Estoque: ", font=("arial 18 bold"))
        self.estoque.place(x=0,y=320)
        self.estoque_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.estoque_entrada.place(x=380,y=320)

        self.preco_produto= Label(master, text="Preço Produto: ", font=("arial 18 bold"))
        self.preco_produto.place(x=0,y=370)
        self.preco_produto_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.preco_produto_entrada.place(x=380,y=370) 
             

        self.btn_voltar = Button(master, text="Voltar", width=10, height=2, bg='green', fg='white', font=("arial 18 bold"))
        self.btn_voltar.place(x=0,y=450)
        self.btn_limpar = Button(master, text="Limpar", width=13, height=2, bg='red', fg='white', font=("arial 18 bold"), command=self.btn_limpar)
        self.btn_limpar.place(x=230,y=450)
        self.btn_cadastrar = Button(master, text="Cadastrar", width=13, height=2, bg='steelblue', fg='white', font=("arial 18 bold"), command= self.btn_cadastrar)
        self.btn_cadastrar.place(x=430,y=450)
        self.btn_atualizar = Button(master, text="Atualizar", width=13, height=2, bg='steelblue', fg='white', font=("arial 18 bold"), command = self.btn_atualizar)
        self.btn_atualizar.place(x=630,y=450)
    
    def pesquisarnome(self, *args, **kwargs):

        self.nome_produto = self.nome_produto_entrada.get()
        
        sql = ("SELECT * FROM PRODUTO WHERE DESCRICAO = ?")             
        resultado = con.execute(sql,(self.nome_produto)) 
        for r in resultado:
            self.n0 = r[0]
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
        self.idproduto_entrada.delete(0,END)              
        self.idproduto_entrada.insert(0,str(self.n0))
        self.nome_produto_entrada.delete(0,END)
        self.nome_produto_entrada.insert(0,str(self.n1))
        self.ativo_entrada.delete(0,END)
        self.ativo_entrada.insert(0,str(self.n2))
        self.datacriado_entrada.delete(0,END)
        self.datacriado_entrada.insert(0,str(self.n3))
        self.estoque_entrada.delete(0,END)
        self.estoque_entrada.insert(0,str(self.n4))        
        self.preco_produto_entrada.delete(0,END)
        self.preco_produto_entrada.insert(0,str(self.n5))

    def pesquisarid(self, *args, **kwargs):

        self.idproduto= self.idproduto_entrada.get()
        
        sql = ("SELECT * FROM PRODUTO WHERE IDPRODUTO = ?")            
        resultado = con.execute(sql,(self.idproduto)) 
        for r in resultado:
            self.n0 = r[0]
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
        
        
        self.idproduto_entrada.delete(0,END)              
        self.idproduto_entrada.insert(0,str(self.n0))
        self.nome_produto_entrada.delete(0,END)
        self.nome_produto_entrada.insert(0,str(self.n1))
        self.ativo_entrada.delete(0,END)
        self.ativo_entrada.insert(0,str(self.n2))
        self.datacriado_entrada.delete(0,END)
        self.datacriado_entrada.insert(0,str(self.n3))
        self.estoque_entrada.delete(0,END)
        self.estoque_entrada.insert(0,str(self.n4))        
        self.preco_produto_entrada.delete(0,END)
        self.preco_produto_entrada.insert(0,str(self.n5))

    def btn_atualizar(self, *args, **kwargs):
        self.u1 = self.nome_produto_entrada.get()
        self.u2 = self.ativo_entrada.get()
        self.u3 = self.datacriado
        self.u4 = self.estoque_entrada.get()
        self.u5 = self.preco_produto_entrada.get()

        query_update = ("UPDATE PRODUTO SET DESCRICAO =?, ATIVO =?, QTDEESTOQUE=?, VALOR =? WHERE IDPRODUTO=?")
        atualizar_resultado = con.execute(query_update,(self.u1, self.u2, self.u4, self.u5, self.idproduto_entrada.get()))
        tkinter.messagebox.showinfo("Sucesso", "Cadastro atualizado")
    
    def btn_limpar(self, *args, **kwargs):
        self.idproduto_entrada.delete(0,END)
        self.nome_produto_entrada.delete(0,END)
        self.ativo_entrada.delete(0,END)
        self.datacriado_entrada.delete(0,END)
        self.estoque_entrada.delete(0,END)
        self.preco_produto_entrada.delete(0,END)
        

    def btn_cadastrar(self, *args, **kwargs):
        self.nome_produto = self.nome_produto_entrada.get()
        self.estoque = self.estoque_entrada.get()
        self.preco_produto = self.preco_produto_entrada.get()
        self.data = datetime.now()
        self.ativo = self.ativo_entrada.get()
        
        if self.nome_produto == '' or self.estoque == '' or self.preco_produto == '':
            tkinter.messagebox.showinfo("Erro","Favor Preencher todos os campos")
        else:
            sql = ("INSERT INTO PRODUTO (DESCRICAO, ATIVO, DATACRIADO, QTDEESTOQUE,VALOR) VALUES(?,?,?,?,?)")
            
            con.execute(sql,(self.nome_produto,self.ativo,self.data,self.estoque, self.preco_produto))            
            tkinter.messagebox.showinfo("Sucesso","Produto Cadastrado")

      

b = Cadastrar(root)
root.mainloop()