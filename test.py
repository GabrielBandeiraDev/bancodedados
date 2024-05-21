from tela_sistema_cadastro_apam.banco import *

result = registration_system.search_apam(1)  # ID de exemplo
if result:
    print(result)
