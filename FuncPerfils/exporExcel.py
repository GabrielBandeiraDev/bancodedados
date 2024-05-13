import pandas as pd

# Função para exportar os dados para um arquivo Excel
def exportar_para_excel(perfil):
    df = pd.DataFrame.from_dict(perfil, orient='index')
    df.to_excel('perfis.xlsx' , index=False)