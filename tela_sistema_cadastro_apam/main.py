# importando dependencias do Tkinter
import tkinter as tk
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from ttkthemes import ThemedTk
from tkinter import scrolledtext


# importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date
from banco import RegistrationSystem
from util import Validacao
# chamdo a view
from banco import *

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul

class Example(ThemedTk):
    """
    Example that is used to create screenshots for new themes.
    """
    def __init__(self, theme="aquativo"):
        """
        :param theme: Theme to show off
        """
        ThemedTk.__init__(self, fonts=True, themebg=True)
        self.set_theme(theme)
        # Create widgets
        self.notebook = ttk.Notebook(self)
        self.notebook.add(ttk.Button(self, text="Hello World"), text="Frame One")
        self.notebook.add(ttk.Button(self, text="Hello Universe"), text="Frame Two")
        self.menu = tk.Menu(self, tearoff=False)


#janelas 
janela = Tk()
janela.title("SISTEMA DE CADASTRO | ASSOCIAÇÃO MATO-GROSSENSE PROTETORA DOS ANIMAIS (APAM)")
janela.geometry('1200x800')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

for i in range(5):
    janela.grid_columnconfigure(i, weight=1)
    
def maximize_window(event=None):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    window_width = janela.winfo_reqwidth()
    window_height = janela.winfo_reqheight()
    # x = (screen_width // 10) - (window_width // 10)
    # y = (screen_height // 5) - (window_height // 5)
    # janela.geometry(f"{window_width}x{window_height}+{x}+{y}")
    

janela.bind("<Configure>", maximize_window)



style = Style(janela)
style.theme_use("clam")

# Frames
frame_logo = Frame(janela, width=1200, height=70, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=150, height=100, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=10, padx=10, sticky=NSEW)

frame_detalhes = Frame(janela, width=885, height=460, bg=co1, relief=SOLID)
frame_detalhes.grid(row=1, column=1, pady=0, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=885, height=1200, bg=co1)
frame_tabela.grid(row=3, column=0, pady=10, padx=10, sticky=NSEW, columnspan=5)


# frame Logo
global imagem, imagem_string, l_imagem

app_lg = Image.open('assets/logo.png')
app_lg = app_lg.resize((65,65))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="APAM - Associação Mato-Grossense Protetora dos Animais", width=1200, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1, padx=20)
app_logo.place(x=5, y=0)


# abrindo a imagem
imagem  = Image.open('assets/logo.png')
imagem = imagem.resize((110, 110))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_detalhes, image=imagem,bg=co1, fg=co4 )
l_imagem.place(x=5, y=343)


# ------------- funcoes para CRUD ---------------

def adicionar():
    global imagem, imagem_string, l_imagem
    
    data_registro = d_data_registro.get()
    email = e_email.get()
    name = n_nome.get()
    cpf = c_cpf.get()
    rg = r_rg.get()
    data_nascimento = d_data_nascimento.get()
    sexo = s_sexo.get()
    naturalidade = n_naturalidade.get()
    estado_civil = e_estado_civil.get()
    endereco = e_endereco.get()
    telefone_fixo = t_telefone_fixo.get()
    telefone_celular = t_telefone_celular.get()
    nome_empresa = n_nome_empresa.get()
    endereco_empresa = e_endereco_empresa.get()
    telefone_empresa = t_telefone_empresa.get()
    profissao = p_profissao.get()
    valor_colaborar = v_valor_colaborar.get()
    em_que_pode_ajudar_apam = e_em_que_pode_ajudar_apam.get("1.0", END)
    outras_formas_de_ajudar_apam = o_outras_formas_de_ajudar_apam.get("1.0", END)
    expectativa_trabalho_volutario = e_expectativa_trabalho_volutario.get("1.0", END)
    imagem = imagem_string
    lista = [data_registro, email, name, cpf, rg, data_nascimento, sexo, naturalidade, estado_civil, endereco, telefone_fixo, telefone_celular, nome_empresa, endereco_empresa, telefone_empresa, profissao, valor_colaborar, em_que_pode_ajudar_apam, outras_formas_de_ajudar_apam, expectativa_trabalho_volutario, imagem]
    
    # for i in lista:
    #     if not Validacao.verificarCampo(i):
    #         messagebox.showerror('Erro', 'Preencha todos os campos')
    #         return

    

    # if not Validacao.validarCPF(cpf):
    #     messagebox.showerror('Erro', 'CPF inválido')
    #     return
    # if not Validacao.validarEmail(email):
    #     messagebox.showerror('Erro', 'Email inválido')
    #     return
    # if not Validacao.validarCEP(endereco):
    #     messagebox.showerror('Erro', 'CEP inválido')
    #     return
    # if not Validacao.validarTelefone_e_Celular(l_telefone_celular):
    #     messagebox.showerror('Erro', 'Telefone/Celular inválido')
    #     return
    # if not Validacao.validarSexo(sexo):
    #     messagebox.showerror('Erro', 'Sexo inválido')
    #     return
    # if not Validacao.validarNome(data_registro):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(email):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(name):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(cpf):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(rg):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(data_nascimento):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(sexo):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(naturalidade):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(estado_civil):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(endereco):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(telefone_fixo):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(nome_empresa):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(nome_empresa):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(endereco_empresa):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(telefone_empresa):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(profissao):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(valor_colaborar):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(em_que_pode_ajudar_apam):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(outras_formas_de_ajudar_apam):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    # if not Validacao.validarNome(expectativa_trabalho_volutario):
    #     messagebox.showerror('Erro', 'Nome inválido')
    #     return
    
   
    # apam = (data_registro, email, name, cpf, rg, data_nascimento, sexo, naturalidade, estado_civil, endereco, telefone_fixo, telefone_celular, nome_empresa, endereco_empresa, telefone_empresa, profissao, valor_colaborar, em_que_pode_ajudar_apam, outras_formas_de_ajudar_apam, expectativa_trabalho_volutario)
    # registration_system.register_apam(apam)
    registration_system.register_apam(lista)
    
    # Limpando campos de entrada
    d_data_registro.delete(0, END)
    e_email.delete(0, END)
    n_nome.delete(0, END)
    c_cpf.delete(0, END)
    r_rg.delete(0, END)
    d_data_nascimento.delete(0, END)
    s_sexo.delete(0, END)
    n_naturalidade.delete(0, END)
    e_estado_civil.delete(0, END)
    e_endereco.delete(0, END)
    t_telefone_fixo.delete(0, END)
    t_telefone_celular.delete(0, END)
    n_nome_empresa.delete(0, END)
    e_endereco_empresa.delete(0, END)
    t_telefone_empresa.delete(0, END)
    p_profissao.delete(0, END)
    v_valor_colaborar.delete(0, END)
    o_outras_formas_de_ajudar_apam.delete("1.0", END)
    e_expectativa_trabalho_volutario.delete("1.0", END)
    e_em_que_pode_ajudar_apam.delete("1.0", END)
    
    mostrar_tabela()


# funcao procurar
def procurar():
	global imagem, imagem_string, l_imagem

	# obtendo o id
	id_apam = int(e_procurar.get())

	# procura o ID do apam
	dados = registration_system.search_apam(id_apam)

	# limpando os campos de entradas
	d_data_registro.delete(0, END)
	e_email.delete(0, END)
	n_nome.delete(0, END)
	c_cpf.delete(0, END)
	r_rg.delete(0, END)
	d_data_nascimento.delete(0, END)
	s_sexo.delete(0, END)
	n_naturalidade.delete(0, END)
	e_estado_civil.delete(0, END)
	e_endereco.delete(0, END)
	t_telefone_fixo.delete(0, END)
	t_telefone_celular.delete(0, END)
	n_nome_empresa.delete(0, END)
	e_endereco_empresa.delete(0, END)
	t_telefone_empresa.delete(0, END)
	p_profissao.delete(0, END)
	v_valor_colaborar.delete(0, END)
	e_em_que_pode_ajudar_apam.delete("1.0", END)
	o_outras_formas_de_ajudar_apam.delete("1.0", END)
	e_expectativa_trabalho_volutario.delete("1.0", END)

	# inser os valores
	d_data_registro.insert(END,dados[1])
	e_email.insert(END,dados[2])
	n_nome.insert(END,dados[3])
	c_cpf.insert(END,dados[4])
	r_rg.insert(END,dados[5])
	d_data_nascimento.insert(END,dados[6])
	s_sexo.insert(END,dados[7])
	n_naturalidade.insert(END,dados[8])
	e_estado_civil.insert(END,dados[9])
	e_endereco.insert(END,dados[10])
	t_telefone_fixo.insert(END,dados[11])
	t_telefone_celular.insert(END,dados[12])
	n_nome_empresa.insert(END,dados[13])
	e_endereco_empresa.insert(END,dados[14])
	t_telefone_empresa.insert(END,dados[15])
	p_profissao.insert(END,dados[16])
	v_valor_colaborar.insert(END,dados[17])
	e_em_que_pode_ajudar_apam.insert(END,dados[18])
	o_outras_formas_de_ajudar_apam.insert(END,dados[19])
	e_expectativa_trabalho_volutario.insert(END,dados[20])
	

	imagem = dados[21]
	imagem_string = imagem


	imagem  = Image.open(imagem)
	imagem = imagem.resize((130, 130))
	imagem = ImageTk.PhotoImage(imagem)

	l_imagem = Label(frame_detalhes, image=imagem,bg=co1, fg=co4 )
	l_imagem.place(x=5, y=343)



def atualizar():
	global imagem, imagem_string, l_imagem

	# obtendo o id
	id_apam = int(e_procurar.get())
 
 	# obtendo os valores
	data_registro = d_data_registro.get()
	email = e_email.get()
	name = n_nome.get()
	cpf = c_cpf.get()
	rg = r_rg.get()
	data_nascimento = d_data_nascimento.get()
	sexo = s_sexo.get()
	naturalidade = n_naturalidade.get()
	estado_civil = e_estado_civil.get()
	endereco = e_endereco.get()
	telefone_fixo = t_telefone_fixo.get()
	telefone_celular = t_telefone_celular.get()
	nome_empresa = n_nome_empresa.get()
	endereco_empresa = e_endereco_empresa.get()
	telefone_empresa = t_telefone_empresa.get()
	profissao = p_profissao.get()
	valor_colaborar = v_valor_colaborar.get()
	em_que_pode_ajudar_apam = e_em_que_pode_ajudar_apam.get("1.0", END)
	outras_formas_de_ajudar_apam = o_outras_formas_de_ajudar_apam.get("1.0", END)
	expectativa_trabalho_volutario = e_expectativa_trabalho_volutario.get("1.0", END)
	imagem = imagem_string

	
	lista = [data_registro, email, name, cpf, rg, data_nascimento, sexo, naturalidade, estado_civil, endereco, telefone_fixo, telefone_celular, nome_empresa, endereco_empresa, telefone_empresa, profissao, valor_colaborar, em_que_pode_ajudar_apam, outras_formas_de_ajudar_apam, expectativa_trabalho_volutario, imagem, id_apam]

	# Verificando caso algum campo esteja vazio ou nao
	for i in lista[-2]:
		if i == '':
			messagebox.showerror('Erro', 'Preencha todos os campos')
			return

	# atualizar cadastro do apam
	registration_system.update_apam(lista)
 
 	# limpando os campos de entradas
	d_data_registro.delete(0, END)
	e_email.delete(0, END)
	n_nome.delete(0, END)
	c_cpf.delete(0, END)
	r_rg.delete(0, END)
	d_data_nascimento.delete(0, END)
	s_sexo.delete(0, END)
	n_naturalidade.delete(0, END)
	e_estado_civil.delete(0, END)
	e_endereco.delete(0, END)
	t_telefone_fixo.delete(0, END)
	t_telefone_celular.delete(0, END)
	n_nome_empresa.delete(0, END)
	e_endereco_empresa.delete(0, END)
	t_telefone_empresa.delete(0, END)
	p_profissao.delete(0, END)
	v_valor_colaborar.delete(0, END)
	e_em_que_pode_ajudar_apam.delete("1.0", END)
	o_outras_formas_de_ajudar_apam.delete("1.0", END)
	e_expectativa_trabalho_volutario.delete("1.0", END)

	# abre a imagem
	imagem  = Image.open('assets/logo.png')
	imagem = imagem.resize((130, 130))
	imagem = ImageTk.PhotoImage(imagem)

	l_imagem = Label(frame_detalhes, image=imagem,bg=co1, fg=co4 )
	l_imagem.place(x=5, y=343)

	# mostrando os valores na Tabela
	mostrar_tabela()



# funcao deletar
def deletar():
	global imagem, imagem_string, l_imagem

	# obtendo o id
	id_apam = int(e_procurar.get())

	# limpando os campos de entradas
	registration_system.delete_apam(id_apam)
	d_data_registro.delete(0, END)
	e_email.delete(0, END)
	n_nome.delete(0, END)
	c_cpf.delete(0, END)
	r_rg.delete(0, END)
	d_data_nascimento.delete(0, END)
	s_sexo.delete(0, END)
	n_naturalidade.delete(0, END)
	e_estado_civil.delete(0, END)
	e_endereco.delete(0, END)
	t_telefone_fixo.delete(0, END)
	t_telefone_celular.delete(0, END)
	n_nome_empresa.delete(0, END)
	e_endereco_empresa.delete(0, END)
	t_telefone_empresa.delete(0, END)
	p_profissao.delete(0, END)
	v_valor_colaborar.delete(0, END)
	e_em_que_pode_ajudar_apam.delete(0, END)
	o_outras_formas_de_ajudar_apam.delete(0, END)
	e_expectativa_trabalho_volutario.delete(0, END)

	e_procurar.delete(0,END)

	# abrindo a imagem
	imagem  = Image.open('assets/logo.png')
	imagem = imagem.resize((130, 130))
	imagem = ImageTk.PhotoImage(imagem)

	l_imagem = Label(frame_detalhes, image=imagem,bg=co1, fg=co4 )
	l_imagem.place(x=5, y=343)

	# mostrando os valores na Tabela
	mostrar_tabela()


l_nome = Label(frame_detalhes, text="NOME *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
n_nome = ttk.Entry(frame_detalhes, width=100, justify='left')
n_nome.place(x=4, y=35)

l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_cpf.place(x=4, y=60)
c_cpf = ttk.Entry(frame_detalhes, width=20, justify='left')
c_cpf.place(x=4, y=84)

l_rg = Label(frame_detalhes, text="RG *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_rg.place(x=197, y=60)
r_rg = ttk.Entry(frame_detalhes, width=20, justify='left')
r_rg.place(x=197, y=84)

l_data_nascimento = Label(frame_detalhes, text="DATA NASC. *", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.place(x=393, y=60)
d_data_nascimento = DateEntry(frame_detalhes, width=15, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2023)
d_data_nascimento.place(x=393, y=84)

l_sexo = Label(frame_detalhes, text="SEXO *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=745, y=60)
s_sexo = ttk.Combobox(frame_detalhes, width=7, font=('Ivy 8 bold'), justify='center', state='readonly')
s_sexo['values'] = ('M','F')
s_sexo.place(x=745, y=85)

l_telefone_fixo = Label(frame_detalhes, text="TELEFONE FIXO *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telefone_fixo.place(x=4, y=109)
t_telefone_fixo = ttk.Entry(frame_detalhes, width=20, justify='left')
t_telefone_fixo.place(x=4, y=134)

l_telefone_celular = Label(frame_detalhes, text="TELEFONE MÓVEL *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telefone_celular.place(x=197, y=109)
t_telefone_celular = ttk.Entry(frame_detalhes, width=20, justify='left')
t_telefone_celular.place(x=197, y=134)

l_naturalidade = Label(frame_detalhes, text="NATURALIDADE *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_naturalidade.place(x=665, y=109)
n_naturalidade = ttk.Entry(frame_detalhes, width=18, justify='left')
n_naturalidade.place(x=665, y=134)

l_email = Label(frame_detalhes, text="EMAIL *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=393, y=109)
e_email = ttk.Entry(frame_detalhes, width=30, justify='left')
e_email.place(x=393, y=134)

l_endereco = Label(frame_detalhes, text="ENDEREÇO *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=4, y=159)
e_endereco = ttk.Entry(frame_detalhes, width=44, justify='left')
e_endereco.place(x=4, y=184)

l_profissao = Label(frame_detalhes, text="PROFISSÃO *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_profissao.place(x=393, y=159)
p_profissao = ttk.Entry(frame_detalhes, width=30, justify='left')
p_profissao.place(x=393, y=184)

l_nome_empresa = Label(frame_detalhes, text="NOME DA EMPRESA *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome_empresa.place(x=4, y=209)
n_nome_empresa = ttk.Entry(frame_detalhes, width=44, justify='left')
n_nome_empresa.place(x=4, y=234)

l_endereco_empresa = Label(frame_detalhes, text="ENDEREÇO DA EMPRESA *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco_empresa.place(x=393, y=209)
e_endereco_empresa = ttk.Entry(frame_detalhes, width=30, justify='left')
e_endereco_empresa.place(x=393, y=234)

l_telefone_empresa = Label(frame_detalhes, text="TELEFONE EMPRESA *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telefone_empresa.place(x=665, y=209)
t_telefone_empresa = ttk.Entry(frame_detalhes, width=10, justify='left')
t_telefone_empresa.place(x=665, y=234)

l_data_registro = Label(frame_detalhes, text="DATA REGISTRO *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_registro.place(x=665, y=159)
d_data_registro = DateEntry(frame_detalhes, width=16, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2023)
d_data_registro.place(x=665, y=184)

l_em_que_pode_ajudar_apam = Label(frame_detalhes, text="EM QUE PODE AJUDAR APAM *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_em_que_pode_ajudar_apam.place(x=4, y=259)
e_em_que_pode_ajudar_apam = scrolledtext.ScrolledText(frame_detalhes, width=48, height=3, wrap=WORD)
e_em_que_pode_ajudar_apam.place(x=4, y=284)

l_outras_formas_de_ajudar_apam = Label(frame_detalhes, text="OUTRAS FORMAS DE AJUDAR APAM *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_outras_formas_de_ajudar_apam.place(x=430, y=345)
o_outras_formas_de_ajudar_apam = scrolledtext.ScrolledText(frame_detalhes, width=46, height=3, wrap=WORD)
o_outras_formas_de_ajudar_apam.place(x=430, y=368)

l_expectativa_trabalho_volutario = Label(frame_detalhes, text="EXPECTATIVA TRABALHO VOLUNTÁRIO *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_expectativa_trabalho_volutario.place(x=430, y=259)
e_expectativa_trabalho_volutario = scrolledtext.ScrolledText(frame_detalhes, width=46, height=3, wrap=WORD)
e_expectativa_trabalho_volutario.place(x=430, y=284)

l_valor_colaborar = Label(frame_detalhes, text="VALOR COLABORAR *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_valor_colaborar.place(x=234, y=345)
v_valor_colaborar = ttk.Entry(frame_detalhes, width=20, justify='left')
v_valor_colaborar.place(x=234, y=368)

# Definindo o widget de entrada i_imagem
i_imagem = ttk.Entry(frame_detalhes, width=30, justify='left')
i_imagem.place(x=665, y=234)

l_estado_civil = Label(frame_detalhes, text="ESTADO CIVIL *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_estado_civil.place(x=558, y=60)
e_estado_civil = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'), state='readonly')
e_estado_civil['values'] = ('Solteiro(a)','Casado(a)','Separado(a)','Divorciado(a)','Viúvo(a)', 'União estável')
e_estado_civil.place(x=558, y=85)

#funcao para escolher imagem

def escolher_imagem():
	global imagem, imagem_string, l_imagem
 
	imagem = fd.askopenfilename()
	imagem_string = imagem

	#abre a imagem
	imagem = Image.open(imagem)
	imagem = imagem.resize((110,110))
	imagem = ImageTk.PhotoImage(imagem)
	l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
	l_imagem.place(x=4, y=343)

	botao_carregar['text'] = 'Trocar de foto'

botao_carregar = Button(frame_detalhes, command=escolher_imagem, text="Carregar Foto".upper(), width=12, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=124, y=368)


# Tabela do banco apam
def mostrar_tabela():

	# area do scrollbars
	list_header = ['id','data_registro', 'email', 'name', 'cpf', 'rg', 'data_nascimento', 'sexo', 'naturalidade', 'estado_civil',
    'endereço', 'telefone_fixo', 'telefone_celular', 'nome_empresa', 'endereco_empresa', 'telefone_empresa', 'profissao',
    'valor_colaborar', 'em_que_pode_ajudar_apam', 'outras_formas_de_ajudar_apam', 'expectativa_trabalho_volutario']
 
	# visualiza as informações do banco apam
	df_list = registration_system.view_all_bancoapam()

	global tree_estado_civil

	tree_apam = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

	# vertical scrollbar
	vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_apam.yview)
	# horizontal scrollbar
	hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_apam.xview)

	tree_apam.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
	tree_apam.grid(column=0, row=1, sticky='nsew')
	vsb.grid(column=1, row=1, sticky='ns')
	hsb.grid(column=0, row=2, sticky='ew')
	frame_tabela.grid_columnconfigure(0, weight=12)

	hd=["center","nw","center","center","center","center","center","center","nw","center","center","nw","center","center","center","center","center","center","center","center","center"]
	h=[116,116,116,116,116,116,60,152,116,136,116,116,116,116,116,116,60,152,116,60,152]
	n=0

	for col in list_header:
		tree_apam.heading(col, text=col.title(), anchor=NW)

		# ajustes das colunas dentro do scrollbar
		tree_apam.column(col, width=h[n],anchor=hd[n])

		n += 1

	for item in df_list:
		tree_apam.insert('', 'end', values=item)



# Procura os dados cadastrados

frame_procurar = Frame(frame_botoes, width=40, height=50, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Realize a Busca pelo  ID ", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center',relief="solid",font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

l_cpf = Label(frame_procurar, text="Realize a Busca pelo  ID ", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_cpf.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center',relief="solid",font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

l_data_nascimento = Label(frame_procurar, text="Realize a Busca pelo  ID ", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center',relief="solid",font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar,command=procurar, anchor=CENTER, text="Procurar", width=9, overrelief=RIDGE,  font=('ivy 7 bold'),bg=co1, fg=co0 )
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

#Botoes

app_img_adicionar = Image.open('assets/add.png')
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar, text=" Adicionar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('assets/update.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes,command=atualizar, image=app_img_atualizar, text=" Atualizar Dados", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open('assets/delete.png')
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, command=deletar, image=app_img_deletar, text=" Deletar", width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# linha separatoria

l_linha = Label(frame_botoes, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
l_linha.place(x=265, y=0)


# ver a tabela de cadastro
mostrar_tabela()

janela.mainloop()