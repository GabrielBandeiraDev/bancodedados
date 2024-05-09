import PySimpleGUI as sg
import pickle
import os

# Função para salvar perfis em um arquivo
def salvar_perfis(perfis):
    with open('perfis.pickle', 'wb') as arquivo:
        pickle.dump(perfis, arquivo)

# Função para carregar perfis do arquivo
def carregar_perfis():
    if os.path.exists('perfis.pickle'):
        with open('perfis.pickle', 'rb') as arquivo:
            return pickle.load(arquivo)
    return {}

# Função para editar informações do perfil
def editar_info(perfil):
    layout_editar = [
        [sg.Text('Nome:'), sg.InputText(perfil.get('Nome', ''), key='edit_nome')],
        [sg.Text('Matrícula:'), sg.InputText(perfil.get('Matricula', ''), key='edit_matricula')],
        [sg.Text('Número de Celular:'), sg.InputText(perfil.get('Celular', ''), key='edit_celular')],
        [sg.Text('Cargo:'), sg.InputText(perfil.get('Cargo', ''), key='edit_cargo')],
        [sg.Text('Idade:'), sg.InputText(perfil.get('Idade', ''), key='edit_idade')],
        [sg.Text('Ministério:'), sg.InputText(perfil.get('Ministerio', ''), key='edit_ministerio')],
        [sg.Button('Salvar')]
    ]

    window_editar = sg.Window('Editar Perfil', layout_editar)

    while True:
        event_editar, values_editar = window_editar.read()

        if event_editar == sg.WIN_CLOSED or event_editar == 'Salvar':
            break

    window_editar.close()

    perfil['Nome'] = values_editar['edit_nome']
    perfil['Matricula'] = values_editar['edit_matricula']
    perfil['Celular'] = values_editar['edit_celular']
    perfil['Cargo'] = values_editar['edit_cargo']
    perfil['Idade'] = values_editar['edit_idade']
    perfil['Ministerio'] = values_editar['edit_ministerio']

# Função para excluir um perfil
def excluir_perfil(nome, perfis):
    if sg.popup_yes_no(f'Deseja excluir o perfil de {nome}?') == 'Yes':
        perfis.pop(nome, None)

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
perfis = carregar_perfis()

# Definição do layout inicial
layout = [
    [sg.Text("Adicionar Nome:"), sg.InputText(key="novo_nome")],
    [sg.Text("Adicionar Matrícula:"), sg.InputText(key="nova_matricula")],
    [sg.Text("Adicionar Número de Celular:"), sg.InputText(key="novo_celular")],
    [sg.Text("Adicionar Cargo:"), sg.InputText(key="novo_cargo")],
    [sg.Text("Adicionar Idade:"), sg.InputText(key="nova_idade")],
    [sg.Text("Adicionar Ministério:"), sg.InputText(key="novo_ministerio")],
    [sg.Button("Adicionar", size=(20, 1))],
    [sg.Listbox(values=list(perfis.keys()), size=(60, 15), key="lista_nomes")],
    [sg.Text("Pesquisar Nome:"), sg.InputText(key="nome_pesquisa")],
    [sg.Text("Pesquisar Matrícula:"), sg.InputText(key="matricula_pesquisa")],
    [sg.Button("Pesquisar por Nome"), sg.Button("Pesquisar por Matrícula")],
    [sg.Text("", size=(60, 1))], 
    [sg.Button("Editar", size=(10, 1)), sg.Button("Excluir", size=(10, 1)),
     sg.Button("Salvar", size=(10, 1)), sg.Button("Carregar", size=(10, 1)),
     sg.Button("Abrir Perfil", size=(10, 1), button_color=('white', 'red'))]
]

# Criar a janela principal
janela_principal = sg.Window("Gerenciador de Perfis", layout, element_justification="c")

while True:
    evento_principal, valores_principal = janela_principal.read()

    if evento_principal == sg.WIN_CLOSED or evento_principal == "Sair":
        salvar_perfis(perfis)  # Salvar perfis antes de sair
        break

    if evento_principal == "Adicionar":
        novo_nome = valores_principal["novo_nome"]
        novo_perfil = {
            "Nome": novo_nome,
            "Matricula": valores_principal["nova_matricula"],
            "Celular": valores_principal["novo_celular"],
            "Cargo": valores_principal["novo_cargo"],
            "Idade": valores_principal["nova_idade"],
            "Ministerio": valores_principal["novo_ministerio"]
        }
        perfis[novo_nome] = novo_perfil

    if evento_principal == "Editar":
        nome_selecionado = valores_principal["lista_nomes"]
        if nome_selecionado:
            perfil_selecionado = perfis.get(nome_selecionado[0])
            if perfil_selecionado:
                editar_info(perfil_selecionado)

    if evento_principal == "Excluir":
        nome_selecionado = valores_principal["lista_nomes"]
        if nome_selecionado:
            excluir_perfil(nome_selecionado[0], perfis)

    if evento_principal == "Abrir Perfil":
        nome_selecionado = valores_principal["lista_nomes"]
        if nome_selecionado:
            perfil = perfis.get(nome_selecionado[0])
            if perfil:
                sobrenome = nome_selecionado[0].split()[-1]  # Última palavra é considerada sobrenome
                parentescos = verificar_parentesco(sobrenome, perfis)
                parentescos_str = f"Parentescos: {', '.join(parentescos)}" if parentescos else ""
                sg.popup(f"Nome: {perfil.get('Nome', 'N/A')}\nMatrícula: {perfil.get('Matricula', 'N/A')}\nNúmero de Celular: {perfil.get('Celular', 'N/A')}\nCargo: {perfil.get('Cargo', 'N/A')}\nIdade: {perfil.get('Idade', 'N/A')}\nMinistério: {perfil.get('Ministerio', 'N/A')}\n{parentescos_str}")

    if evento_principal == "Pesquisar por Nome":
        nome_pesquisa = valores_principal["nome_pesquisa"]
        if nome_pesquisa:
            perfil = perfis.get(nome_pesquisa)
            if perfil:
                sg.popup(f"Nome: {perfil.get('Nome', 'N/A')}\nMatrícula: {perfil.get('Matricula', 'N/A')}\nNúmero de Celular: {perfil.get('Celular', 'N/A')}\nCargo: {perfil.get('Cargo', 'N/A')}\nIdade: {perfil.get('Idade', 'N/A')}\nMinistério: {perfil.get('Ministerio', 'N/A')}")

    if evento_principal == "Pesquisar por Matrícula":
        matricula_pesquisa = valores_principal["matricula_pesquisa"]
        if matricula_pesquisa:
            nome_encontrado = pesquisar_por_matricula(matricula_pesquisa, perfis)
            if nome_encontrado:
                perfil = perfis.get(nome_encontrado)
                sg.popup(f"Nome: {perfil.get('Nome', 'N/A')}\nMatrícula: {perfil.get('Matricula', 'N/A')}\nNúmero de Celular: {perfil.get('Celular', 'N/A')}\nCargo: {perfil.get('Cargo', 'N/A')}\nIdade: {perfil.get('Idade', 'N/A')}\nMinistério: {perfil.get('Ministerio', 'N/A')}")

    janela_principal["lista_nomes"].update(values=list(perfis.keys()))

janela_principal.close()
