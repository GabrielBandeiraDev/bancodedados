import tkinter as tk
from tkinter import messagebox
import exporExcel

def ver_perfil(perfis, listbox_nomes):
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    perfil_selecionado = perfis.get(nome_selecionado)
    if perfil_selecionado:
        messagebox.showinfo("Informações do Perfil", f"Informações de {nome_selecionado}:\n\n{perfil_selecionado}")

        exporExcel.exportar_para_excel(perfis)