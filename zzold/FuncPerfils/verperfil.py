import tkinter as tk

def ver_perfil(perfis, listbox_nomes):
    nome_selecionado = listbox_nomes.get(tk.ACTIVE)
    perfil_selecionado = perfis.get(nome_selecionado)
    if perfil_selecionado:
        # Create a new tkinter window
        window = tk.Tk()
        window.title(f"Perfil de {nome_selecionado}")
              
        # Create labels for each key-value pair in the profile dictionary
        row = 1
        for chave, valor in perfil_selecionado.items():
            label_chave = tk.Label(window, text=chave + ":")
            label_valor = tk.Label(window, text=valor)
            label_chave.grid(row=row, column=0, sticky="w")
            label_valor.grid(row=row, column=1, sticky="w")
            row += 1
        
        # Run the tkinter event loop
        window.mainloop()