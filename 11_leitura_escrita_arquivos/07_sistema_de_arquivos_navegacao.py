"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar 
e fazer uso do módulo oa.

os -> Operating System - Sistema Operacional


# getcwd() -> pega o current work directory - diretório de trabalho concorrente
# Retorna o path (caminho) absoluto
print(os.getcwd()) # C:\\Users\\gabrielg\\Downloads\\Mystudies

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..') # volta uma 'casa'
print(os.getcwd()) # C:\\Users\\gabrielg\\Downloads

os.chdir('..') 
print(os.getcwd()) # C:\\Users\\gabrielg
    
os.chdir('..') 
print(os.getcwd()) # C:\\Users

os.chdir('..') 
print(os.getcwd()) # C:
    
os.chdir('..') 
print(os.getcwd()) # C:
    
    
# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('\\EstudosPython\\11_leitura_escrita_arquivos')) # True


# OBS para usuário Windows
# Se voce, infelizmente, estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users')) # True  



# Fazer o import 
import os

# Podemos identificar o sistema operacional com o módulo os

print(os.name) # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional

print(os.sys())  


# Fazer o import
import sys

print(sys.platform)



# '/home/geek/workspace/sistema'

print(os.getcwd()) # 'C:\\Users\\gabrielg\\Downloads\\Mystudies'

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd()) # 'C:\\Users\\gabrielg\\Downloads\\Mystudies\\geek\\university'

# Veja que o os.path.join() recebe dois parametros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntando ao atual.

# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir()) 
"""

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = (os.scandir())

arquivos = list(scanner)

#print(arquivos)

#print(dir(arquivos[0]))

print(arquivos[0].inode()) # ??
print(arquivos[0].is_dir()) # É um diretório? False
print(arquivos[0].is_file()) # É um arquivo? True
print(arquivos[0].is_symlink()) # É um link simbólico False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # Estátisicas...

# OBS: Quando utilizamos a função scandir() nós precisaos fechá-la, assim quando abrimos um arquivo.

scanner.close()