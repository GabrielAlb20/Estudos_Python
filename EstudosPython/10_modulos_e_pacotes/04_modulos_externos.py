"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Packge

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org/


colorama -> É utilizado para permitir impressão de textos coloridos no terminal.


Instalando um módulo colorama

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.RED+ 'Geek University')
print(Fore.WHITE+ 'Geek University')
print(Fore.LIGHTGREEN_EX+ 'Geek University')



"""

import pydf
pdf = pydf.generate_pdf('<h1>Geek University</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
