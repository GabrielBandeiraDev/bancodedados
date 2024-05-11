import tkinter as tk
from tkinter import messagebox
import pandas as pd
from FuncPerfils.data_management import salvar_perfil
from FuncPerfils.carregaPerfil import carrega_perfil


# Função para editar informações do perfil
def editar_info(perfil):
    def salvar():
        perfil['Nome'] = edit_nome.get()
        perfil['Matricula'] = edit_matricula.get()
        perfil['Celular'] = edit_celular.get()
        perfil['Cargo'] = edit_cargo.get()
        perfil['Idade'] = edit_idade.get()
        perfil['Ministerio'] = edit_ministerio.get()
        window_editar.destroy()

        # Após salvar as edições, exportar para o Excel
        exportar_para_excel()

    window_editar = tk.Toplevel()
    window_editar.title('Editar Perfil')

    edit_nome = tk.Entry(window_editar)
    edit_nome.insert(0, perfil.get('Nome', ''))
    edit_nome.grid(row=0, column=1)
    tk.Label(window_editar, text='Nome:').grid(row=0, column=0)

    edit_matricula = tk.Entry(window_editar)
    edit_matricula.insert(0, perfil.get('Matricula', ''))
    edit_matricula.grid(row=1, column=1)
    tk.Label(window_editar, text='Matrícula:').grid(row=1, column=0)

    edit_celular = tk.Entry(window_editar)
    edit_celular.insert(0, perfil.get('Celular', ''))
    edit_celular.grid(row=2, column=1)
    tk.Label(window_editar, text='Número de Celular:').grid(row=2, column=0)

    edit_cargo = tk.Entry(window_editar)
    edit_cargo.insert(0, perfil.get('Cargo', ''))
    edit_cargo.grid(row=3, column=1)
    tk.Label(window_editar, text='Cargo:').grid(row=3, column=0)

    edit_idade = tk.Entry(window_editar)
    edit_idade.insert(0, perfil.get('Idade', ''))
    edit_idade.grid(row=4, column=1)
    tk.Label(window_editar, text='Idade:').grid(row=4, column=0)

    edit_ministerio = tk.Entry(window_editar)
    edit_ministerio.insert(0, perfil.get('Ministerio', ''))
    edit_ministerio.grid(row=5, column=1)
    tk.Label(window_editar, text='Ministério:').grid(row=5, column=0)

    btn_salvar = tk.Button(window_editar, text='Salvar', command=salvar)
    btn_salvar.grid(row=6, column=0, columnspan=2)

# Função para excluir um perfil
def excluir_perfil():
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    if messagebox.askyesno('Excluir Perfil', f'Deseja excluir o perfil de {nome_selecionado}?'):
        listbox_nomes.delete(tk.ACTIVE)
        perfis.pop(nome_selecionado, None)
        salvar_perfil(perfis)
        
        # Após excluir o perfil, exportar para o Excel
        exportar_para_excel()

# Função para pesquisar por matrícula
def pesquisar_por_matricula(matricula, perfis):
    for nome, perfil in perfis.items():
        if perfil.get("Matricula") == matricula:
            return nome
    return None

# Função para verificar parentesco pelo sobrenome
def verificar_parentesco(sobrenome, perfis):
    parentescos = []
    for nome, perfil in perfis.items():
        if sobrenome in nome and nome != sobrenome:  # Evitar coincidência exata
            parentescos.append(nome)
    return parentescos

# Inicialização dos perfis
perfis = carrega_perfil()

# Função para adicionar um novo perfil
def adicionar_perfil():
    novo_nome = entry_nome.get()
    novo_perfil = {
        "Nome": novo_nome,
        "Matricula": entry_matricula.get(),
        "Celular": entry_celular.get(),
        "Cargo": entry_cargo.get(),
        "Idade": entry_idade.get(),
        "Ministerio": entry_ministerio.get()
    }
    perfis[novo_nome] = novo_perfil
    listbox_nomes.insert(tk.END, novo_nome)
    salvar_perfil(perfis)
    
    # Após adicionar o perfil, exportar para o Excel
    exportar_para_excel()

# Função para exibir todas as informações de um perfil
def ver_perfil():
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    perfil_selecionado = perfis.get(nome_selecionado)
    if perfil_selecionado:
        messagebox.showinfo("Informações do Perfil", f"Informações de {nome_selecionado}:\n\n{perfil_selecionado}")
        
        # Após ver o perfil, exportar para o Excel
        exportar_para_excel()

# Função para exportar os dados para um arquivo Excel
def exportar_para_excel():
    df = pd.DataFrame.from_dict(perfis, orient='index')
    df.to_excel('perfis.xlsx')

# Criar a janela principal
janela_principal = tk.Tk()
janela_principal.title('Gerenciador de Perfis')

# Widgets
tk.Label(janela_principal, text='Adicionar Nome:').grid(row=0, column=0)
entry_nome = tk.Entry(janela_principal)
entry_nome.grid(row=0, column=1)

tk.Label(janela_principal, text='Adicionar Matrícula:').grid(row=1, column=0)
entry_matricula = tk.Entry(janela_principal)
entry_matricula.grid(row=1, column=1)

tk.Label(janela_principal, text='Adicionar Número de Celular:').grid(row=2, column=0)
entry_celular = tk.Entry(janela_principal)
entry_celular.grid(row=2, column=1)

tk.Label(janela_principal, text='Adicionar Cargo:').grid(row=3, column=0)
entry_cargo = tk.Entry(janela_principal)
entry_cargo.grid(row=3, column=1)

tk.Label(janela_principal, text='Adicionar Idade:').grid(row=4, column=0)
entry_idade = tk.Entry(janela_principal)
entry_idade.grid(row=4, column=1)

tk.Label(janela_principal, text='Adicionar Ministério:').grid(row=5, column=0)
entry_ministerio = tk.Entry(janela_principal)
entry_ministerio.grid(row=5, column=1)

btn_adicionar = tk.Button(janela_principal, text='Adicionar', command=adicionar_perfil)
btn_adicionar.grid(row=6, column=0, columnspan=2)

btn_excluir = tk.Button(janela_principal, text='Excluir', command=excluir_perfil)
btn_excluir.grid(row=7, column=0, columnspan=2)

btn_ver_perfil = tk.Button(janela_principal, text='Ver Perfil', command=ver_perfil)
btn_ver_perfil.grid(row=8, column=0, columnspan=2)

listbox_nomes = tk.Listbox(janela_principal, width=60, height=15)
listbox_nomes.grid(row=10, column=0, columnspan=2)

# Adicionando nomes existentes na Listbox
for nome in perfis.keys():
    listbox_nomes.insert(tk.END, nome)

janela_principal.mainloop()
