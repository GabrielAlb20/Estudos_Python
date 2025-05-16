"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizemos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro 
de entrada, que neste caso é o nome do arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro FileNotFoundError


<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -. Modo de Leitura. r -> read() -> ler

"""

# Exemplo

#arquivo = open('texto.txt')

#print(arquivo)

#print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

#ret = arquivo.read()

#print(type(ret))

#print(ret)

#print(arquivo.read())

# print(arquivo.read())

# OBS: O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# OBS: A função read() lê todo o conteúdo do arquivo.

