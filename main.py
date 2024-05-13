import tkinter as tk
from tkinter import messagebox
import pandas as pd
from FuncPerfils.data_management import salvar_perfil
from FuncPerfils.carregaPerfil import carrega_perfil
from FuncPerfils.perfilMatri import pesquisar_por_matricula
from FuncPerfils.exporExcel import exportar_para_excel



# Função para editar informações do perfil
def salvar(perfil, perfis):
    perfil['Nome'] = edit_nome.get()
    perfil['Matricula'] = edit_matricula.get()
    perfil['Celular'] = edit_celular.get()
    perfil['Cargo'] = edit_cargo.get()
    perfil['Idade'] = edit_idade.get()
    perfil['Ministerio'] = edit_ministerio.get()
    window_editar.destroy()

    # Após salvar as edições, exportar para o Excel
    exporExcel.exportar_para_excel(perfis)  # Chamando a função corretamente


# Função para excluir um perfil
def excluir_perfil():
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    if messagebox.askyesno('Excluir Perfil', f'Deseja excluir o perfil de {nome_selecionado}?'):
        listbox_nomes.delete(tk.ACTIVE)
        perfis.pop(nome_selecionado, None)
        salvar_perfil(perfis)

        # Após excluir o perfil, exportar para o Excel
        exporExcel.exportar_para_excel(perfis)  # Chamando a função corretamente


# Função para pesquisar por matrícula

# Inicialização dos perfis
perfis = carrega_perfil()


# Restante do seu código...


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
    exportar_para_excel(perfis)

# Função para exibir todas as informações de um perfil
def ver_perfil():
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    perfil_selecionado = perfis.get(nome_selecionado)
    if perfil_selecionado:
        messagebox.showinfo("Informações do Perfil", f"Informações de {nome_selecionado}:\n\n{perfil_selecionado}")
        
        # Após ver o perfil, exportar para o Excel
        exportar_para_excel(perfis)

# # Função para exportar os dados para um arquivo Excel (FUNÇÃO ALOCADA PARA O exporExcel.py)

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
btn_pesquisar_matricula.grid(row=9, column=0, columnspan=2)

# Adicionando os botões "Salvar" e "Excluir" de volta na janela principal
btn_adicionar = tk.Button(janela_principal, text='Adicionar', command=adicionar_perfil)
btn_adicionar.grid(row=6, column=0, columnspan=2)

btn_excluir = tk.Button(janela_principal, text='Excluir', command=excluir_perfil)
btn_excluir.grid(row=7, column=0, columnspan=2)

btn_ver_perfil = tk.Button(janela_principal, text='Ver Perfil', command=ver_perfil)
btn_ver_perfil.grid(row=8, column=0, columnspan=2)


listbox_nomes = tk.Listbox(janela_principal, width=60, height=15)
listbox_nomes.grid(row=10, column=0, columnspan=2)

janela_principal.mainloop()

# Adicionando nomes existentes na Listbox
for nome in perfis.keys():
    listbox_nomes.insert(tk.END, nome)

janela_principal.mainloop()