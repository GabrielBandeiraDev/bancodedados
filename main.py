import tkinter as tk
from tkinter import messagebox
from FuncPerfils.data_management import salvar_perfil
from FuncPerfils.carregaPerfil import carrega_perfil
from FuncPerfils.perfilMatri import pesquisar_por_matricula
from FuncPerfils.exporExcel import exportar_para_excel
from FuncPerfils.verperfil import ver_perfil
from FuncPerfils.excluirPerfil import excluir_perfil
from FuncPerfils.editarinfo import editar_info


# Função para editar informações do perfil
# Preciso que vc crie o def salvar com os mesmo campos do adicionar perfil
# funcao para salvar as informacoes

    




def salvar(perfil, perfis):
    perfil['Nome'] = edit_nome.get()
    perfil['Matricula'] = edit_matricula.get()
    perfil['Celular'] = edit_numero_celular.get()
    perfil['Número fixo'] = edit_numero_fixo.get()
    perfil['Telefone da empresa de trabalho'] = edit_fixo_empresa.get()
    perfil['Cargo'] = edit_cargo.get()
    perfil['Data de Nascimento'] = edit_data_nascimento.get()
    perfil['Data'] = edit_data.get()
    perfil['CPF'] = edit_cpf.get()
    perfil['RG'] = edit_rg.get()
    perfil['Gênero'] = edit_genero.get()
    perfil['Email'] = edit_endereco_email.get()
    perfil['Endereço completo'] = edit_endereco_completo.get()
    perfil['Nome da empresa de trabalho'] = edit_nome_empresa.get()
    perfil['Profissão'] = edit_profissao.get()
    perfil['Naturalidade'] = edit_naturalidade.get()
    perfil['Endereço da empresa de trabalho'] = edit_endereco_empresa.get()
    perfil['Com qual valor mensal poderia colaborar?'] = edit_valor_mensal.get()
    perfil['Estado Civil'] = edit_estado_civil.get() 
     
    window_editar.destroy()

    # Após salvar as edições, exportar para o Excel
    exportar_para_excel(perfis)  # Chamando a função corretamente

def adicionar_perfil():
    novo_nome = entry_nome.get()
    novo_perfil = {
        "Nome": novo_nome,
        "Matricula": entry_matricula.get(),
        "Celular": entry_numero_celular.get(),
        "Número fixo": entry_numero_fixo.get(),
        "Telefone da empresa de trabalho": entry_fixo_empresa.get(),
        "Cargo": entry_cargo.get(),
        "Data de Nascimento": entry_data_nascimento.get(),
        "Data": entry_data.get(),
        "CPF": entry_cpf.get(),
        "RG": entry_rg.get(),
        "Gênero": entry_genero.get(),
        "Email": entry_endereco_email.get(),
        "Endereço completo": entry_endereco_completo.get(),
        "Nome da empresa de trabalho": entry_nome_empresa.get(),
        "Profissão": entry_profissao.get(),
        "Naturalidade": entry_naturalidade.get(),
        "Endereço da empresa de trabalho": entry_endereco_empresa.get(),
        "Com qual valor mensal poderia colaborar?": entry_valor_mensal.get(),
        "Estado Civil": entry_estado_civil.get()
    }
    perfis[novo_nome] = novo_perfil
    listbox_nomes.insert(tk.END, novo_nome)
    salvar_perfil(perfis)
    # Após adicionar o perfil, exportar para o Excel
    exportar_para_excel(perfis)


# Função para exibir todas as informações de um perfil
def ver_perfil():
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    perfil_selecionado = perfis.get(nome_selecionado)
    if perfil_selecionado:
        messagebox.showinfo("Informações do Perfil", f"Informações de {nome_selecionado}:\n\n{perfil_selecionado}")

        # Após ver o perfil, exportar para o Excel
        exportar_para_excel(perfis)


# Função para editar informações do perfil
def editar_informacao():
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    perfil_selecionado = perfis.get(nome_selecionado)
    if perfil_selecionado:
        # Chamar a função editar_info
        editar_info(perfil_selecionado, perfis)


# Inicialização dos perfis
perfis = carrega_perfil()

# Criar a janela principal
janela_principal = tk.Tk()
janela_principal.title('Gerenciador de Perfis')

# Widgets
tk.Label(janela_principal, text='Nome Completo:').grid(row=0, column=0)
entry_nome = tk.Entry(janela_principal)
entry_nome.grid(row=0, column=1)

tk.Label(janela_principal, text='Matrícula:').grid(row=1, column=0)
entry_matricula = tk.Entry(janela_principal)
entry_matricula.grid(row=1, column=1)

tk.Label(janela_principal, text='Número de Celular:').grid(row=2, column=0)
entry_numero_celular = tk.Entry(janela_principal)
entry_numero_celular.grid(row=2, column=1)

tk.Label(janela_principal, text='Número fixo:').grid(row=3, column=0)
entry_numero_fixo = tk.Entry(janela_principal)
entry_numero_fixo.grid(row=3, column=1)

tk.Label(janela_principal, text='Telefone da empresa de trabalho:').grid(row=4, column=0)
entry_fixo_empresa = tk.Entry(janela_principal)
entry_fixo_empresa.grid(row=4, column=1)

tk.Label(janela_principal, text='Cargo:').grid(row=5, column=0)
entry_cargo = tk.Entry(janela_principal)
entry_cargo.grid(row=5, column=1)

tk.Label(janela_principal, text='Data de Nascimento:').grid(row=6, column=0)
entry_data_nascimento = tk.Entry(janela_principal)
entry_data_nascimento.grid(row=6, column=1)

tk.Label(janela_principal, text='Data:').grid(row=7, column=0)
entry_data = tk.Entry(janela_principal)
entry_data.grid(row=7, column=1)

tk.Label(janela_principal, text='CPF:').grid(row=8, column=0)
entry_cpf = tk.Entry(janela_principal)
entry_cpf.grid(row=8, column=1)

tk.Label(janela_principal, text='RG:').grid(row=9, column=0)
entry_rg = tk.Entry(janela_principal)
entry_rg.grid(row=9, column=1)

tk.Label(janela_principal, text='Gênero:').grid(row=10, column=0)
entry_genero = tk.Entry(janela_principal)
entry_genero.grid(row=10, column=1)

tk.Label(janela_principal, text='Email:').grid(row=11, column=0)
entry_endereco_email = tk.Entry(janela_principal)
entry_endereco_email.grid(row=11, column=1)

tk.Label(janela_principal, text='Endereço completo:').grid(row=12, column=0)
entry_endereco_completo = tk.Entry(janela_principal)
entry_endereco_completo.grid(row=12, column=1)

tk.Label(janela_principal, text='Nome da empresa de trabalho:').grid(row=13, column=0)
entry_nome_empresa = tk.Entry(janela_principal)
entry_nome_empresa.grid(row=13, column=1)

tk.Label(janela_principal, text='Profissão:').grid(row=14, column=0)
entry_profissao = tk.Entry(janela_principal)
entry_profissao.grid(row=14, column=1)

tk.Label(janela_principal, text='Naturalidade:').grid(row=15, column=0)
entry_naturalidade = tk.Entry(janela_principal)
entry_naturalidade.grid(row=15, column=1)

tk.Label(janela_principal, text='Endereço da empresa de trabalho:').grid(row=16, column=0)
entry_endereco_empresa = tk.Entry(janela_principal)
entry_endereco_empresa.grid(row=16, column=1)

tk.Label(janela_principal, text='Com qual valor mensal poderia colaborar?:').grid(row=17, column=0)
entry_valor_mensal = tk.Entry(janela_principal)
entry_valor_mensal.grid(row=17, column=1)

tk.Label(janela_principal, text='Estado Civil:').grid(row=18, column=0)
entry_estado_civil = tk.Entry(janela_principal)
entry_estado_civil.grid(row=18, column=1)



def pesquisar_matricula():
    def pesquisar():
        matricula = entry_matricula_pesquisa.get()
        perfil_encontrado = pesquisar_por_matricula(matricula)
        if perfil_encontrado:
            messagebox.showinfo("Perfil Encontrado", f"Nome: {perfil_encontrado}")
        else:
            messagebox.showinfo("Perfil não encontrado", f"Nenhum perfil encontrado para a matrícula {matricula}")

    window_pesquisar = tk.Toplevel()
    window_pesquisar.title('Pesquisar Matrícula')

    tk.Label(window_pesquisar, text='Matrícula:').grid(row=0, column=0)
    entry_matricula_pesquisa = tk.Entry(window_pesquisar)
    entry_matricula_pesquisa.grid(row=0, column=1)

    btn_pesquisar = tk.Button(window_pesquisar, text='Pesquisar', command=pesquisar)
    btn_pesquisar.grid(row=1, column=0, columnspan=2)


btn_pesquisar_matricula = tk.Button(janela_principal, text='Pesquisar Matrícula', command=pesquisar_matricula)
btn_pesquisar_matricula.grid(row=19, column=0, columnspan=2)

# Adicionando os botões "Salvar", "Excluir", "Ver Perfil" e "Editar Informação"
btn_adicionar = tk.Button(janela_principal, text='Adicionar', command=adicionar_perfil)
btn_adicionar.grid(row=20, column=0, columnspan=2)

btn_excluir = tk.Button(janela_principal, text='Excluir', command=lambda: excluir_perfil(listbox_nomes, perfis))
btn_excluir.grid(row=21, column=0, columnspan=2)

btn_ver_perfil = tk.Button(janela_principal, text='Ver Perfil', command=ver_perfil)
btn_ver_perfil.grid(row=22, column=0, columnspan=2)

btn_editar_info = tk.Button(janela_principal, text='Editar Informação', command=editar_informacao)
btn_editar_info.grid(row=23, column=0, columnspan=2)

listbox_nomes = tk.Listbox(janela_principal, width=60, height=15)
listbox_nomes.grid(row=24, column=0, columnspan=2)

# Adicionando nomes existentes na Listbox
for nome in perfis.keys():
    listbox_nomes.insert(tk.END, nome)

janela_principal.mainloop()
