import tkinter as tk
from tkinter import messagebox
from FuncPerfils.exporExcel import exportar_para_excel

def ver_perfil(perfis, listbox_nomes):
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    print("Nome selecionado:", nome_selecionado)  # Mensagem de depuração
    perfil_selecionado = perfis.get(nome_selecionado)
    print("Perfil selecionado:", perfil_selecionado)  # Mensagem de depuração
    if perfil_selecionado:
        messagebox.showinfo("Informações do Perfil", f"Informações de {nome_selecionado}:\n\n{perfil_selecionado}")
        exportar_para_excel(perfis)
