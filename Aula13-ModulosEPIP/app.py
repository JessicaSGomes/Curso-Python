# MÓDULO: é um arquivo contendo definições e instruções Python
# MÓDULO: pode conter tanto instruções executáveis quanto definições de funções e classes.

import tools

# para acessar: tools.nomedavariavel/função
print(tools.PI)
print(tools.GRAVITY)
print(tools.get_extension("test.txt"))
print(tools.highest_number([1, -2, 5, 7, 0, -45, 3]))
print("-------------- FIM DO MÓDULO ------------")

# PIP (qual a versão? terminal: pip --version)
# http://docs.python.org/3/py-modindex.html lista de modulos em python ja disponíveis para usar
# pip é o sistema de gerenciamento de pacotes para Python. 
# é usado para instalar, atualizar e gerenciar pacotes (bibliotecas e módulos) escritos em Python
# permite que os dev instalem e gerenciem bibliotecas e frameworks de maneira eficiente

# COMANDOS COMUNS   

# pip install nome-do-pacote -> instalar o pacote
# pip install beautifulsoup4 -t ./libs 
# -t define o diretório de destino e .\libs indica que será instalado no diretório 'libs'
# pip uninstall beautifulsoup4 -> desistala o pacote

# criar arquivo requirements.txt -> listar as bibliotecas que quer instalar 
# pip install -r .\requirements.txt -t .\libs -> irá instalar as bibliotecas listadas no requirements.txt
# pip list -> lista os pacotes instalados
