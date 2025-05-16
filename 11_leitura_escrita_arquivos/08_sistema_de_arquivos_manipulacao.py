"""
Sistema de arquivos manipulação



# Descobrindo se um arquivo ou diretório existe

print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('texto.txt'))   # True


# Diretório

# Paths relativos
print(os.path.exists('geek')) # True
print(os.path.exists('geek/university')) # True
print(os.path.exists('geek/university/geek3.py')) # True
print(os.path.exists('outro')) # False

# Paths absolutos
print(os.path.exists('/home/geek/university')) # False
print(os.path.exists('/home/geek/Images')) # True


# Criando arquivos

# Forma 1
open('arquivo.txt', 'w').close()

# Forma 2
open('arquivo_teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass # <- vou fazer nada, "passo" só pra não gerar erro de identação.


# Criando arquivos

#os.mknod('arquivo-teste4.txt')

# os.mknod('arquivo-teste4.txt')

# OBS: Se voce estiver utilizando no Mac OS, pode haver um erro de PermissionError

# OBS: Criando um arquivo mknod() se o arquivo já existir teremos o erro FileExistsError.

# OBS: Esse método acima é exclusivo para sistemas Unix (Linux e macOS) e não está disponível para windows


# Versão para Windows.
nome_arquivo = 'arquivo-teste4.txt'

try:
    with open(nome_arquivo, 'w') as arquivo:
        pass  # Não escrevemos nada no arquivo, apenas o criamos vazio
    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro ao criar o arquivo: {e}")
    
    
import os
# Path Relativo
os.mkdir("templates")


# Path Absoluto
os.mkdir('C:\\Users\\gabrielg\\Downloads\\Mystudies')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

import os

os.mkdir('/etc/templates')

# OBS: Se não tivermos permissão para criar os diretórios, teremos um PermissionError


#os.mkdir('templates')

#os.mkdir('templates\\geek')

#os.mkdir('templates\\geek\\university')

# Desse modo é mais demorado e exige mais código
# com apenas esse trecho abaixo voce tem o mesmo resultado, mas com menos código e mais fácil

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates\\geek\\university')
# OBS: Se já existir, teremos um FileExistsError

os.makedirs('templates2\\novo2\\outro2', exist_ok=True)



# Renomear arquivos e diretórios

os.rename('templates2', 'geek')

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError


# Arquivo
os.rename('geek2\\novo2\\outro2\\teste.txt')


# Renomear arquivos e diretórios

# Arquivos 
os.rename('frutas.txt', 'cesta.txt')


# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles
# não vão para a lixeira. Eles somem.

# Deletar arquivos

os.remove('cesta.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos IsADirectoryError



import os

# Removendo diretórios vazios

os.rmdir('geek')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError



# Removendo uma árvora de diretórios

for arquivo in os.scandir('geek'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)
 #   if not arquivo.is_file():
      #  os.rmdir(arquivo.path)
      
# DELETA  TODOS OS ARQUIVOS DENTRO DE UMA PASTA



# Podemos remover uma árvora de diretórios vazios

os.removedirs('geek\\mais')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.


SENÃO CONSEGUIR INSTALAR o send2trash, utilize: sudo apt-get install lsb-core


os.remove('cesta1.txt') # Não vai para a lixeira. É deletado imediatamente


import os

# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeira)
from send2trash import send2trash

send2trash('cesta2.txt') # Vai pra lixeira. Pode ser restaurado.

send2trash('teste') (Diretório: Vai pra lixeira. Pode ser restaurado.)

# OBS: Se o arquivo não existir, teremos um OSError




# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek Univesity\n')
    input()
    
# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos un input() só para mantermos 
# os arquivos temporários 'vivos' dentro dos blocos with.



# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos 'b'


# Sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()



# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close() # Não podemos esquecer de fechar.


https://docs.python.org/pt-br/3/library/os.html

"""

