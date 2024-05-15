import tkinter as tk

from FuncPerfils.exporExcel import exportar_para_excel
def editar_info(perfil, perfis):
    def salvar():
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


        exportar_para_excel(perfis)



    window_editar = tk.Toplevel()
    window_editar.title('Editar Perfil')
    
    edit_nome = tk.Entry(window_editar)
    edit_nome.insert(0, perfil.get('Nome', ''))
    edit_nome.grid(row=0, column=1)
    tk.Label(window_editar, text='Nome:').grid(row=0, column=0)
    
    edit_matricula = tk.Entry(window_editar)
    edit_matricula.insert(0, perfil.get('Matricula', ''))
    edit_matricula.grid(row=1, column=1)
    tk.Label(window_editar, text='Matricula:').grid(row=1, column=0)
    
    edit_numero_celular = tk.Entry(window_editar)
    edit_numero_celular.insert(0, perfil.get('Celular', ''))
    edit_numero_celular.grid(row=2, column=1)
    tk.Label(window_editar, text='Celular:').grid(row=2, column=0)
    
    edit_numero_fixo = tk.Entry(window_editar)
    edit_numero_fixo.insert(0, perfil.get('Número fixo', ''))
    edit_numero_fixo.grid(row=3, column=1)
    tk.Label(window_editar, text='Número fixo:').grid(row=3, column=0)
    
    edit_fixo_empresa = tk.Entry(window_editar)
    edit_fixo_empresa.insert(0, perfil.get('Telefone da empresa de trabalho', ''))
    edit_fixo_empresa.grid(row=4, column=1)
    tk.Label(window_editar, text='Telefone da empresa de trabalho:').grid(row=4, column=0)
    
    edit_cargo = tk.Entry(window_editar)
    edit_cargo.insert(0, perfil.get('Cargo', ''))
    edit_cargo.grid(row=5, column=1)
    tk.Label(window_editar, text='Cargo:').grid(row=5, column=0)
    
    edit_data_nascimento = tk.Entry(window_editar)
    edit_data_nascimento.insert(0, perfil.get('Data de Nascimento', ''))
    edit_data_nascimento.grid(row=6, column=1)
    tk.Label(window_editar, text='Data de Nascimento:').grid(row=6, column=0)
    
    edit_data = tk.Entry(window_editar)
    edit_data.insert(0, perfil.get('Data', ''))
    edit_data.grid(row=7, column=1)
    tk.Label(window_editar, text='Data:').grid(row=7, column=0)
    
    edit_cpf = tk.Entry(window_editar)
    edit_cpf.insert(0, perfil.get('CPF', ''))
    edit_cpf.grid(row=8, column=1)
    tk.Label(window_editar, text='CPF:').grid(row=8, column=0)
    
    edit_rg = tk.Entry(window_editar)
    edit_rg.insert(0, perfil.get('RG', ''))
    edit_rg.grid(row=9, column=1)
    tk.Label(window_editar, text='RG:').grid(row=9, column=0)
    
    edit_genero = tk.Entry(window_editar)
    edit_genero.insert(0, perfil.get('Gênero', ''))
    edit_genero.grid(row=10, column=1)
    tk.Label(window_editar, text='Gênero:').grid(row=10, column=0)
    
    edit_endereco_email = tk.Entry(window_editar)
    edit_endereco_email.insert(0, perfil.get('Email', ''))
    edit_endereco_email.grid(row=11, column=1)
    tk.Label(window_editar, text='Email:').grid(row=11, column=0)
    
    edit_endereco_completo = tk.Entry(window_editar)
    edit_endereco_completo.insert(0, perfil.get('Endereço completo', ''))
    edit_endereco_completo.grid(row=12, column=1)
    tk.Label(window_editar, text='Endereço completo:').grid(row=12, column=0)
    
    edit_nome_empresa = tk.Entry(window_editar)
    edit_nome_empresa.insert(0, perfil.get('Nome da empresa de trabalho', ''))
    edit_nome_empresa.grid(row=13, column=1)
    tk.Label(window_editar, text='Nome da empresa de trabalho:').grid(row=13, column=0)
    
    edit_profissao = tk.Entry(window_editar)
    edit_profissao.insert(0, perfil.get('Profissão', ''))
    edit_profissao.grid(row=14, column=1)
    tk.Label(window_editar, text='Profissão:').grid(row=14, column=0)
    
    edit_naturalidade = tk.Entry(window_editar)
    edit_naturalidade.insert(0, perfil.get('Naturalidade', ''))
    edit_naturalidade.grid(row=15, column=1)
    tk.Label(window_editar, text='Naturalidade:').grid(row=15, column=0)
    
    edit_endereco_empresa = tk.Entry(window_editar)
    edit_endereco_empresa.insert(0, perfil.get('Endereço da empresa de trabalho', ''))
    edit_endereco_empresa.grid(row=16, column=1)
    tk.Label(window_editar, text='Endereço da empresa de trabalho:').grid(row=16, column=0)
    
    edit_valor_mensal = tk.Entry(window_editar)
    edit_valor_mensal.insert(0, perfil.get('Com qual valor mensal poderia colaborar?', ''))
    edit_valor_mensal.grid(row=17, column=1)
    tk.Label(window_editar, text='Com qual valor mensal poderia colaborar?:').grid(row=17, column=0)
    
    edit_estado_civil = tk.Entry(window_editar)
    edit_estado_civil.insert(0, perfil.get('Estado Civil', ''))
    edit_estado_civil.grid(row=18, column=1)
    tk.Label(window_editar, text='Estado Civil:').grid(row=18, column=0)
    
    btn_salvar = tk.Button(window_editar, text='Salvar', command=salvar)
    btn_salvar.grid(row=19, column=0, columnspan=2)