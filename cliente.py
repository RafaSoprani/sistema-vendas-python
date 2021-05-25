from tkinter import *
import tkinter
import tkinter.messagebox
import sqlalchemy
import pandas as pd
from datetime import datetime

root = Tk()
root.title("Clientes")
root.geometry('870x980+0+0')


server =  '127.0.0.1'
database = 'OPE'
username = 'sa'
password = '9970568'
driver = 'ODBC Driver 17 for SQL Server'
database_con = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"

engine = sqlalchemy.create_engine(database_con)
con = engine.connect()


resultado = pd.read_sql_query("SELECT TOP 1 (IDCLIENTE) FROM CLIENTE ORDER BY IDCLIENTE DESC",con)
for r in resultado:
    IDCLIENTE=r[0]
class Cliente_endereco:
    def __init__(self,master,*args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Clientes", font=("arial 36 bold"), fg="black")
        self.heading.pack(anchor=CENTER)

        self.IDCLIENTE = Label(master, text="ID: ", font=("arial 18 bold"))
        self.IDCLIENTE.place(x=0,y=90)
        self.IDCLIENTE_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.IDCLIENTE_entrada.place(x=380,y=90)
        self.btn_pesquisarid = Button(master, text="Pesquisar", width=12, height=1, bg='orange', font=("arial 12 bold"), command= self.pesquisarid)
        self.btn_pesquisarid.place(x=720,y=90)

        self.nome_cliente = Label(master, text="Nome Cliente:", font=("arial 18 bold"))
        self.nome_cliente.place(x=0,y=140)
        self.nome_cliente_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.nome_cliente_entrada.place(x=380,y=140)
        self.btn_pesquisarnome = Button(master, text="Pesquisar", width=12, height=1, bg='orange', font=("arial 12 bold"), command =self.pesquisarnome)
        self.btn_pesquisarnome.place(x=720,y=140)

        self.CPF_CNPJ= Label(master, text="CPF/CNPJ: ", font=("arial 18 bold"))
        self.CPF_CNPJ.place(x=0,y=190)
        self.CPF_CNPJ_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.CPF_CNPJ_entrada.place(x=380,y=190)
        self.btn_pesquisarcpf_cnpj = Button(master, text="Pesquisar", width=12, height=1, bg='orange', font=("arial 12 bold"), command =self.pesquisarcpfcnpj)
        self.btn_pesquisarcpf_cnpj.place(x=720,y=190)
        
        self.data_nascimento = Label(master, text="Data Nascimento: ", font=("arial 18 bold"))
        self.data_nascimento.place(x=0,y=240)
        self.data_nascimento_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.data_nascimento_entrada.place(x=380,y=240)  

        self.email = Label(master, text="EMAIL: ", font=("arial 18 bold"))
        self.email.place(x=0,y=290)
        self.email_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.email_entrada.place(x=380,y=290) 

        self.RG = Label(master, text="RG: ", font=("arial 18 bold"))
        self.RG.place(x=0,y=340)
        self.RG_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.RG_entrada.place(x=380,y=340) 

        self.tipo_endereco = Label(master, text="Tipo Endereço: ", font=("arial 18 bold"))
        self.tipo_endereco.place(x=0,y=390)
        self.tipo_endereco_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.tipo_endereco_entrada.place(x=380,y=390)

        self.logradouro = Label(master, text="Logradouro: ", font=("arial 18 bold"))
        self.logradouro.place(x=0,y=440)
        self.logradouro_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.logradouro_entrada.place(x=380,y=440)

        self.numero_endereco = Label(master, text="Número: ", font=("arial 18 bold"))
        self.numero_endereco.place(x=0,y=490)
        self.numero_endereco_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.numero_endereco_entrada.place(x=380,y=490)

        self.complemento = Label(master, text="Complemento: ", font=("arial 18 bold"))
        self.complemento.place(x=0,y=540)
        self.complemento_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.complemento_entrada.place(x=380,y=540)

        self.CEP = Label(master, text="CEP: ", font=("arial 18 bold"))
        self.CEP.place(x=0,y=590)
        self.CEP_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.CEP_entrada.place(x=380,y=590)

        self.numero_telefone = Label(master, text="Número telefone: ", font=("arial 18 bold"))
        self.numero_telefone.place(x=0,y=640)
        self.numero_telefone_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.numero_telefone_entrada.place(x=380,y=640)

        self.tipo_telefone = Label(master, text="Tipo telefone: ", font=("arial 18 bold"))
        self.tipo_telefone.place(x=0,y=690)
        self.tipo_telefone_entrada = Entry(master, width=25, font=("arial 18 bold"))
        self.tipo_telefone_entrada.place(x=380,y=690)

        self.btn_voltar = Button(master, text="Voltar", width=10, height=2, bg='green', fg='white', font=("arial 18 bold"))
        self.btn_voltar.place(x=0,y=880)
        self.btn_limpar = Button(master, text="Limpar", width=13, height=2, bg='red', fg='white', font=("arial 18 bold"), command=self.btn_limpar)
        self.btn_limpar.place(x=230,y=880)
        self.btn_cadastrar = Button(master, text="Cadastrar", width=13, height=2, bg='steelblue', fg='white', font=("arial 18 bold"), command= self.btn_cadastrar)
        self.btn_cadastrar.place(x=430,y=880)
        self.btn_atualizar = Button(master, text="Atualizar", width=13, height=2, bg='steelblue', fg='white', font=("arial 18 bold"), command = self.btn_atualizar)
        self.btn_atualizar.place(x=630,y=880)

    
        
    def pesquisarnome(self, *args, **kwargs):

        self.nome_cliente = self.nome_cliente_entrada.get()
        
        sql = ("SELECT * FROM CLIENTE WHERE NOME = ?")             
        resultado = con.execute(sql,(self.nome_cliente)) 
        for r in resultado:
            self.n0 = r[0]
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
            self.n10 = r[10]
            self.n11 = r[11]
            self.n12 = r[12]
        self.IDCLIENTE_entrada.delete(0,END)              
        self.IDCLIENTE_entrada.insert(0,str(self.n0))
        self.nome_cliente_entrada.delete(0,END)
        self.nome_cliente_entrada.insert(0,str(self.n1))
        self.CPF_CNPJ_entrada.delete(0,END)
        self.CPF_CNPJ_entrada.insert(0,str(self.n2))
        self.email_entrada.delete(0,END)
        self.email_entrada.insert(0,str(self.n3))
        self.data_nascimento_entrada.delete(0,END)
        self.data_nascimento_entrada.insert(0,str(self.n4))        
        self.RG_entrada.delete(0,END)
        self.RG_entrada.insert(0,str(self.n5))
        self.tipo_endereco_entrada.delete(0,END)
        self.tipo_endereco_entrada.insert(0,str(self.n6))
        self.logradouro_entrada.delete(0,END)
        self.logradouro_entrada.insert(0,str(self.n7))
        self.numero_endereco_entrada.delete(0,END)
        self.numero_endereco_entrada.insert(0,str(self.n8))
        self.complemento_entrada.delete(0,END)
        self.complemento_entrada.insert(0,str(self.n9))
        self.CEP_entrada.delete(0,END)
        self.CEP_entrada.insert(0,str(self.n10))
        self.numero_telefone_entrada.delete(0,END)
        self.numero_telefone_entrada.insert(0,str(self.n11))
        self.tipo_telefone_entrada.delete(0,END)
        self.tipo_telefone_entrada.insert(0,str(self.n12))
    
    def pesquisarcpfcnpj(self, *args, **kwargs):

        self.CPF_CNPJ = self.CPF_CNPJ_entrada.get()
        
        sql = ("SELECT * FROM CLIENTE WHERE CPF_CNPJ = ?")             
        resultado = con.execute(sql,(self.CPF_CNPJ)) 
        for r in resultado:
            self.n0 = r[0]
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
            self.n10 = r[10]
            self.n11 = r[11]
            self.n12 = r[12]
        self.IDCLIENTE_entrada.delete(0,END)              
        self.IDCLIENTE_entrada.insert(0,str(self.n0))
        self.nome_cliente_entrada.delete(0,END)
        self.nome_cliente_entrada.insert(0,str(self.n1))
        self.CPF_CNPJ_entrada.delete(0,END)
        self.CPF_CNPJ_entrada.insert(0,str(self.n2))
        self.email_entrada.delete(0,END)
        self.email_entrada.insert(0,str(self.n3))
        self.data_nascimento_entrada.delete(0,END)
        self.data_nascimento_entrada.insert(0,str(self.n4))        
        self.RG_entrada.delete(0,END)
        self.RG_entrada.insert(0,str(self.n5))
        self.tipo_endereco_entrada.delete(0,END)
        self.tipo_endereco_entrada.insert(0,str(self.n6))
        self.logradouro_entrada.delete(0,END)
        self.logradouro_entrada.insert(0,str(self.n7))
        self.numero_endereco_entrada.delete(0,END)
        self.numero_endereco_entrada.insert(0,str(self.n8))
        self.complemento_entrada.delete(0,END)
        self.complemento_entrada.insert(0,str(self.n9))
        self.CEP_entrada.delete(0,END)
        self.CEP_entrada.insert(0,str(self.n10))
        self.numero_telefone_entrada.delete(0,END)
        self.numero_telefone_entrada.insert(0,str(self.n11))
        self.tipo_telefone_entrada.delete(0,END)
        self.tipo_telefone_entrada.insert(0,str(self.n12))

    def pesquisarid(self, *args, **kwargs):

        self.IDCLIENTE = self.IDCLIENTE_entrada.get()
        
        sql = ("SELECT * FROM CLIENTE WHERE IDCLIENTE = ?")             
        resultado = con.execute(sql,(self.IDCLIENTE)) 
        for r in resultado:
            self.n0 = r[0]
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
            self.n10 = r[10]
            self.n11 = r[11]
            self.n12 = r[12]
        self.IDCLIENTE_entrada.delete(0,END)              
        self.IDCLIENTE_entrada.insert(0,str(self.n0))
        self.nome_cliente_entrada.delete(0,END)
        self.nome_cliente_entrada.insert(0,str(self.n1))
        self.CPF_CNPJ_entrada.delete(0,END)
        self.CPF_CNPJ_entrada.insert(0,str(self.n2))
        self.email_entrada.delete(0,END)
        self.email_entrada.insert(0,str(self.n3))
        self.data_nascimento_entrada.delete(0,END)
        self.data_nascimento_entrada.insert(0,str(self.n4))        
        self.RG_entrada.delete(0,END)
        self.RG_entrada.insert(0,str(self.n5))
        self.tipo_endereco_entrada.delete(0,END)
        self.tipo_endereco_entrada.insert(0,str(self.n6))
        self.logradouro_entrada.delete(0,END)
        self.logradouro_entrada.insert(0,str(self.n7))
        self.numero_endereco_entrada.delete(0,END)
        self.numero_endereco_entrada.insert(0,str(self.n8))
        self.complemento_entrada.delete(0,END)
        self.complemento_entrada.insert(0,str(self.n9))
        self.CEP_entrada.delete(0,END)
        self.CEP_entrada.insert(0,str(self.n10))
        self.numero_telefone_entrada.delete(0,END)
        self.numero_telefone_entrada.insert(0,str(self.n11))
        self.tipo_telefone_entrada.delete(0,END)
        self.tipo_telefone_entrada.insert(0,str(self.n12))

    def btn_atualizar(self, *args, **kwargs):
        self.IDCLIENTE= self.IDCLIENTE_entrada.get()
        self.u1 = self.nome_cliente_entrada.get()
        self.u2 = self.CPF_CNPJ_entrada.get()
        self.u3 = self.email_entrada.get()
        self.u4 = self.data_nascimento_entrada.get()
        self.u5 = self.RG_entrada.get()
        self.u6 = self.tipo_endereco_entrada.get()
        self.u7 = self.logradouro_entrada.get()
        self.u8 = self.numero_endereco_entrada.get()
        self.u9 = self.complemento_entrada.get()
        self.u10 = self.CEP_entrada.get()
        self.u11 = self.numero_telefone_entrada.get()
        self.u12 = self.tipo_telefone_entrada.get()

        query_update = ("UPDATE CLIENTE SET NOME =?, CPF_CNPJ=?,EMAIL=?, DATANASC=?,RG=?, TIPO_ENDERECO=?, LOGRADOURO=?, NUMERO_ENDERECO=?, COMPLEMENTO=?, CEP=?, NUMERO_TELEFONE=?, TIPO_TELEFONE=? WHERE IDCLIENTE =?")
        atualizar_resultado = con.execute(query_update,(self.u1, self.u2, self.u3, self.u4, self.u5, self.u6,self.u7,self.u8,self.u9,self.u10,self.u11,self.u12, self.IDCLIENTE))
        tkinter.messagebox.showinfo("Sucesso", "Cadastro atualizado")    
    
    
    def btn_cadastrar(self, *args, **kwargs):

        self.nome_cliente = self.nome_cliente_entrada.get()
        self.CPF_CNPJ = self.CPF_CNPJ_entrada.get()
        self.data_nascimento = self.data_nascimento_entrada.get()
        self.email = self.email_entrada.get()
        self.RG = self.RG_entrada.get()
        self.tipo_endereco = self.tipo_endereco_entrada.get()
        self.logradouro = self.logradouro_entrada.get()
        self.numero_endereco = self.numero_endereco_entrada.get()
        self.complemento = self.complemento_entrada.get()
        self.CEP = self.CEP_entrada.get()
        self.numero_telefone = self.numero_telefone_entrada.get()
        self.tipo_telefone = self.tipo_telefone_entrada.get()
        
        if self.nome_cliente == '' or self.CPF_CNPJ == '' or self.data_nascimento == '' or self.logradouro or self.numero_endereco or self.CEP or self.numero_telefone:
            tkinter.messagebox.showinfo("Erro","Favor Preencha os campos Nome, CPF, Data Nascimento, Endereço e telefone")
        else:
            sql_cliente = ("INSERT INTO CLIENTE (NOME, CPF_CNPJ,  DATANASC, EMAIL,RG, TIPO_ENDERECO, LOGRADOURO, NUMERO_ENDERECO, COMPLEMENTO, CEP, NUMERO_TELEFONE, TIPO_TELEFONE) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)")            
            con.execute(sql_cliente,(self.nome_cliente,self.CPF_CNPJ, self.data_nascimento,self.email, self.RG, self.tipo_endereco, self.logradouro,self.numero_endereco, self.complemento,self.CEP,self.numero_telefone,self.tipo_telefone))
            tkinter.messagebox.showinfo("Sucesso", "Cliente atualizado") 

    def btn_limpar(self, *args, **kwargs):
        self.IDCLIENTE_entrada.delete(0,END)
        self.nome_cliente_entrada.delete(0,END)
        self.CPF_CNPJ_entrada.delete(0,END)
        self.email_entrada.delete(0,END)
        self.data_nascimento_entrada.delete(0,END)
        self.email_entrada.delete(0,END)
        self.RG_entrada.delete(0,END) 
        self.tipo_endereco_entrada.delete(0,END)
        self.logradouro_entrada.delete(0,END)
        self.numero_endereco_entrada.delete(0,END)
        self.complemento_entrada.delete(0,END)
        self.CEP_entrada.delete(0,END)
        self.numero_telefone_entrada.delete(0,END)
        self.tipo_telefone_entrada.delete(0,END)


b = Cliente_endereco(root)
root.mainloop()