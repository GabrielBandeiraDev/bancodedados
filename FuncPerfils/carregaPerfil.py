import os
import pickle

# Função para carregar perfis do arquivo
def carrega_perfil():
    if os.path.exists('perfis.pickle'):
        with open('perfis.pickle', 'rb') as arquivo:
            return pickle.load(arquivo)
    return {}
