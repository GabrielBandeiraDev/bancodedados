#

def pesquisar_por_matricula(matricula, perfis):
    for nome, perfil in perfis.items():
        if perfil.get("Matricula") == matricula:
            return nome
    return {}

