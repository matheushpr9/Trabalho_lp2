from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image 

import requests

import sqlite3
con = sqlite3.connect("star_saudavel.db")

cur = con.cursor()

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.nome_entry.delete(0, END)
        self.data_nascimento_entry.delete(0, END)
        # self.id_entry.delete(0, END)
        self.tel_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.num_entry.delete(0, END)
        self.complemento_entry.delete(0, END)

    def navega_cadastro(self):
        for widgets in self.root.winfo_children():
          widgets.destroy()
        Cadastro()

    def navega_menu(self):
        for widgets in self.root.winfo_children():
          widgets.destroy()
        Menu()

    def novoCadastro(self):
        try:

            r = requests.get('https://viacep.com.br/ws/{}/json/'.format(self.cep_entry.get()))
            r = r.json()
            informacoes = {
                "cpf" : self.cpf_entry.get(), 
                "nome_cliente" : self.nome_entry.get(), 
                "telefone" : self.tel_entry.get(), 
                "data_nascimento" :self.data_nascimento_entry.get(), 
                "cep" : self.cep_entry.get(),
                "estado" : r["uf"],
                "cidade":  r["localidade"],
                "bairro" : r["bairro"],
                "logradouro" : r["logradouro"],
                "num" : self.num_entry.get(),
                "complemento" : self.complemento_entry.get()
            }
            try:
                cur.execute("INSERT INTO cliente VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(informacoes["cpf"],informacoes["nome_cliente"],informacoes["telefone"],informacoes["data_nascimento"],informacoes["cep"],informacoes["estado"],informacoes["cidade"],informacoes["bairro"],informacoes["logradouro"],informacoes["num"],informacoes["complemento"] ))
                con.commit()
                messagebox.showinfo("cep válido", informacoes)
            except:
                 messagebox.showerror(f"Usuário já cadastrado", "O Usuário {self.nome_entry.get()}, já foi cadastrado!")
        except:
            messagebox.showerror(f"CEP inválido", "O CEP {self.cep_entry.get()}, não foi encontrado!\nTente usar um formato válido. Ex: 12916-560")

            


    def apagarCadastro(self):
        try:
            id = self.cpf_entry.get()
            cur.execute("DELETE FROM cliente WHERE cpf='{}'".format(id))
            messagebox.showinfo("Cliente excluido", "informacoes")
        except:
            try:
            #id medico
                pass
            except:
                messagebox.showerror(f"CEP inválido", "Médico ou clliente não encontrado")
    def consultaCadastro(self):
        try:
            id = self.cpf_entry.get()
            cur.execute("SELECT * FROM cliente WHERE cpf ='{}'".format(id))
            cliente = cur.fetchall() 
            cliente

            self.limpa_tela()
            self.cpf_entry.insert(0,id)
            self.nome_entry.insert(0, cliente[0][1])
            self.data_nascimento_entry.insert(0, cliente[0][2])
            self.tel_entry.insert(0, cliente[0][3])
            self.cep_entry.insert(0, cliente[0][4])
            self.num_entry.insert(0, cliente[0][5])
            self.complemento_entry.insert(0, cliente[0][6])

        except:
            pass

    def salvaAlteracaoCadastro(self):
        try:
            id = self.cpf_entry.get()
            cur.execute("DELETE FROM cliente WHERE cpf='{}'".format(id))
            self.novoCadastro()
            messagebox.showinfo("Cliente Atualizado", "Cliente {} atualizado com sucesso".format(self.nome_entry.get()))
        except:
            pass

class Menu(Funcs):
    
    def __init__(self):
        self.root = root
        self.tela()
        self.div_tela()
        root.mainloop()
        
    def tela(self):
        self.root.title("Star saudável || Menu") #Definindo nome da janela
        self.root.configure(background='White') #Definindo cor de fundo
        self.root.geometry("700x500") #Configurando tamanho da janela
        self.root.resizable(True, True) #Permitindo redimensionar a janela 
        self.root.maxsize(width=988, height=788) #Limitando o maior tamanho da janela
        self.root.minsize(width= 500, height= 400)
        self.img =Image.open('assets//background.jpg')
        self.bg = ImageTk.PhotoImage(self.img)
        # Add image
        label1 = Label(self.root, image=self.bg)
        label1.place(x = 0,y = 0)

    def div_tela(self):
    
        # Add text
        label2 = Label(self.root, text = "Star saudável",
                    font=("Times New Roman", 48))

        label2.pack(pady = 50)

        # Create Frame
        frame1 = Frame(self.root)
        frame1.pack(pady = 20 )

        # Add buttons
        button1 = Button(frame1,text="Cadastros", font=("Times New Roman", 34), command= self.navega_cadastro)
        button1.pack(pady=5)      

        # Add buttons
        button2 = Button(frame1,text="Gráficos", font=("Times New Roman", 34), command= self.navega_cadastro)
        button2.pack(pady=5)      
    



class Cadastro(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.div_tela()
        self.criando_botoes()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title("Star saudável || Cadastros") #Definindo nome da janela
        self.root.configure(background='White') #Definindo cor de fundo
        self.root.geometry("850x650") #Configurando tamanho da janela
        self.root.resizable(True, True) #Permitindo redimensionar a janela 
        self.root.maxsize(width=988, height=788) #Limitando o maior tamanho da janela
        self.root.minsize(width= 500, height= 400)
        self.img =Image.open('assets//background.jpg')
        self.bg = ImageTk.PhotoImage(self.img)
        # Add image
        label1 = Label(self.root, image=self.bg)
        label1.place(x = 0,y = 0)

    def div_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = "LightSteelBlue", highlightbackground= "LightPink", highlightthickness= 3)
        self.frame_1.place(relx = 0.1, rely= 0.04, relwidth= 0.8, relheight= 0.5) #0 esquerdo, 1 direito
        self.frame_2 = Frame(self.root, bd = 4, bg = "LightSteelBlue", highlightbackground= "LightPink", highlightthickness= 3)
        self.frame_2.place(relx = 0.1, rely= 0.56, relwidth= 0.8, relheight= 0.4) #0 esquerdo, 1 direito

    def criando_botoes(self):
        self.bt_menu = Button(self.frame_1, text="Voltar\nMenu", bd= 2, bg = 'MistyRose',command= self.navega_menu)
        self.bt_menu.place(relx= 0.05, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criando botão cadastrar
        self.bt_cadastar = Button(self.frame_1, text="Novo", bd= 2, bg = 'MistyRose',command= self.novoCadastro)
        self.bt_cadastar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criando botão buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd= 2, bg = 'MistyRose', command=self.consultaCadastro)
        self.bt_buscar.place(relx= 0.35, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criando botão apagar
        self.bt_alterar = Button(self.frame_1, text="Salvar", bd= 2, bg = 'MistyRose', command= self.salvaAlteracaoCadastro)
        self.bt_alterar.place(relx= 0.5, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criando botão alterar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd= 2, bg = 'MistyRose',command= self.apagarCadastro)
        self.bt_apagar.place(relx= 0.65, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criando botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd= 2, bg = 'MistyRose', command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criação de label para colocar ID_Cliente e ID_Médico
        # self.lb_id = Label(self.frame_1, text="ID")
        # self.lb_id.place(relx= 0.05, rely= 0.05)

        # self.id_entry = Entry(self.frame_1)
        # self.id_entry.place(relx = 0.05, rely= 0.2, relwidth= 0.07)

        #Criando label para colocar nome
        self.lb_nome = Label(self.frame_1, text="Nome")
        self.lb_nome.place(relx= 0.05, rely= 0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx = 0.05, rely= 0.425, relwidth= 0.6)

        #Criando label para colocar data de nascimento
        self.data_nascimento = Label(self.frame_1, text="Data de nascimento")
        self.data_nascimento.place(relx= 0.7,  rely= 0.35)

        self.data_nascimento_entry = Entry(self.frame_1)
        self.data_nascimento_entry.place(relx = 0.7, rely= 0.425, relwidth= 0.2)

        #Criando label e entrada do telefone
        self.lb_tel = Label(self.frame_1, text="Telefone")
        self.lb_tel.place(relx = 0.05, rely = 0.525)

        self.tel_entry = Entry(self.frame_1)
        self.tel_entry.place(relx = 0.05, rely = 0.6, relheight= 0.09)

        #Criando label e entrada do CPF
        self.lb_cpf = Label(self.frame_1, text="CPF")
        self.lb_cpf.place(relx= 0.5, rely= 0.525)

        self.cpf_entry = Entry(self.frame_1)
        self.cpf_entry.place(relx= 0.5, rely= 0.6, relwidth= 0.4)

        #Criando label e entrada do telefone
        self.lb_cep = Label(self.frame_1, text="CEP")
        self.lb_cep.place(relx = 0.05, rely = 0.725)

        self.cep_entry = Entry(self.frame_1)
        self.cep_entry.place(relx = 0.05, rely = 0.8, relheight= 0.09)

        #Criando label e entrada do telefone
        self.lb_num = Label(self.frame_1, text="Número")
        self.lb_num.place(relx = 0.4, rely = 0.725)

        self.num_entry = Entry(self.frame_1)
        self.num_entry.place(relx = 0.4, rely = 0.8, relheight= 0.09)

        #Criando label e entrada do telefone
        self.lb_complemento = Label(self.frame_1, text="Complemento")
        self.lb_complemento.place(relx = 0.7, rely = 0.725)

        self.complemento_entry = Entry(self.frame_1)
        self.complemento_entry.place(relx = 0.7, rely = 0.8, relheight= 0.09)

    def lista_frame2(self):
        #Alterando o segundo frame e definindo as colunas
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, column = ("col1", "col2", "col3", "col4"))
        self.listaCli.heading ("#0", text="")
        self.listaCli.heading ("#1", text= "ID")
        self.listaCli.heading ("#2", text= "Nome")
        self.listaCli.heading ("#3", text= "Telefone")
        self.listaCli.heading ("#4", text= "CPF")

        self.listaCli.column("#0", width= 1)
        self.listaCli.column("#1", width= 50)
        self.listaCli.column("#2", width= 200)
        self.listaCli.column("#3", width= 125)
        self.listaCli.column("#4", width= 125)

        self.listaCli.place(relx= 0.01, rely= 0.1, relwidth= 0.95, relheight= 0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient ='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx= 0.92, rely= 0.12, relwidth= 0.036, relheight= 0.82)


    
        

Menu()
