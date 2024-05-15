import tkinter as tk

from FuncPerfils.exporExcel import exportar_para_excel
def editar_info(perfil, perfis):
    def salvar():
        perfil['Nome'] = edit_nome.get()
        perfil['Matricula'] = edit_matricula.get()
        perfil['Celular'] = edit_celular.get()
        perfil['Cargo'] = edit_cargo.get()
        perfil['Idade'] = edit_idade.get()
        perfil['Ministerio'] = edit_ministerio.get()
        window_editar.destroy()


        exportar_para_excel(perfis)

    window_editar = tk.Toplevel()
    window_editar.title('Editar Perfil')

    edit_nome = tk.Entry(window_editar)
    edit_nome.insert(0, perfil.get('Nome', ''))
    edit_nome.grid(row=0, column=1)
    tk.Label(window_editar, text='Nome:').grid(row=0, column=0)

    edit_matricula = tk.Entry(window_editar)
    edit_matricula.insert(0, perfil.get('Matricula', ''))
    edit_matricula.grid(row=1, column=2)
    tk.Label(window_editar, text='Matrícula:').grid(row=1, column=0)

    edit_celular = tk.Entry(window_editar)
    edit_celular.insert(0, perfil.get('Celular', ''))
    edit_celular.grid(row=2, column=3)
    tk.Label(window_editar, text='Número de Celular:').grid(row=2, column=0)

    edit_cargo = tk.Entry(window_editar)
    edit_cargo.insert(0, perfil.get('Cargo', ''))
    edit_cargo.grid(row=3, column=4)
    tk.Label(window_editar, text='Cargo:').grid(row=3, column=0)

    edit_idade = tk.Entry(window_editar)
    edit_idade.insert(0, perfil.get('Idade', ''))
    edit_idade.grid(row=4, column=5)
    tk.Label(window_editar, text='Idade:').grid(row=4, column=0)

    edit_ministerio = tk.Entry(window_editar)
    edit_ministerio.insert(0, perfil.get('Ministerio', ''))
    edit_ministerio.grid(row=5, column=6)
    tk.Label(window_editar, text='Ministério:').grid(row=5, column=0)

    btn_salvar = tk.Button(window_editar, text='Salvar', command=salvar)
    btn_salvar.grid(row=6, column=0, columnspan=2)