import tkinter as tk
from tkinter import messagebox
from FuncPerfils.data_management import salvar_perfil
from FuncPerfils.exporExcel import exportar_para_excel

def excluir_perfil(listbox_nomes, perfis):
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    if messagebox.askyesno('Excluir Perfil', f'Deseja excluir o perfil de {nome_selecionado}?'):
        listbox_nomes.delete(tk.ACTIVE)
        perfis.pop(nome_selecionado, None)
        salvar_perfil(perfis)

        # Após excluir o perfil, exportar para o Excel
        exportar_para_excel(perfis)
