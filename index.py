from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.nome_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.tel_entry.delete(0, END)
        self.cpf_entry.delete(0, END)

    def navega_cadastro(self):
        for widgets in self.root.winfo_children():
          widgets.destroy()
        Cadastro()

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
        self.img =Image.open('C:\\Users\\matheus.ptasinski\\Downloads\\background_star_saudavel.png')
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
        self.img =Image.open('C:\\Users\\matheus.ptasinski\\Downloads\\background_star_saudavel.png')
        self.bg = ImageTk.PhotoImage(self.img)
        # Add image
        label1 = Label(self.root, image=self.bg)
        label1.place(x = 0,y = 0)

    def div_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = "LightSteelBlue", highlightbackground= "LightPink", highlightthickness= 3)
        self.frame_1.place(relx = 0.1, rely= 0.06, relwidth= 0.8, relheight= 0.4) #0 esquerdo, 1 direito
        self.frame_2 = Frame(self.root, bd = 4, bg = "LightSteelBlue", highlightbackground= "LightPink", highlightthickness= 3)
        self.frame_2.place(relx = 0.1, rely= 0.5, relwidth= 0.8, relheight= 0.4) #0 esquerdo, 1 direito

    def criando_botoes(self):
        #Criando botão cadastrar
        self.bt_cadastar = Button(self.frame_1, text="Novo", bd= 2, bg = 'MistyRose')
        self.bt_cadastar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criando botão buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd= 2, bg = 'MistyRose')
        self.bt_buscar.place(relx= 0.35, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criando botão apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd= 2, bg = 'MistyRose')
        self.bt_apagar.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criando botão alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd= 2, bg = 'MistyRose')
        self.bt_alterar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criando botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd= 2, bg = 'MistyRose', command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criação de label para colocar ID_Cliente e ID_Médico
        self.lb_id = Label(self.frame_1, text="ID")
        self.lb_id.place(relx= 0.05, rely= 0.05)

        self.id_entry = Entry(self.frame_1)
        self.id_entry.place(relx = 0.05, rely= 0.2, relwidth= 0.07)

        #Criando label para colocar nome
        self.lb_nome = Label(self.frame_1, text="Nome")
        self.lb_nome.place(relx= 0.05, rely= 0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx = 0.05, rely= 0.5, relwidth= 0.9)

        #Criando label e entrada do telefone
        self.lb_tel = Label(self.frame_1, text="Telefone")
        self.lb_tel.place(relx = 0.05, rely = 0.65)

        self.tel_entry = Entry(self.frame_1)
        self.tel_entry.place(relx = 0.05, rely = 0.8, relheight= 0.09)

        #Criando label e entrada do CPF
        self.lb_cpf = Label(self.frame_1, text="CPF")
        self.lb_cpf.place(relx= 0.5, rely= 0.65)

        self.cpf_entry = Entry(self.frame_1)
        self.cpf_entry.place(relx= 0.5, rely= 0.8, relwidth= 0.4)

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
