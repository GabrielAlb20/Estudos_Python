'''
Módulo Collections - Default Dict

# Recap Dicionários

dicionario = {'curso': 'Programaçao em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

# print(dicionario["outro"]) # ??? KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que nao houver 
um valor definido. caso tentemos acessar uma chave que nao existe, essa chave sera criada\
e o valor default será atribuido

# OBS: Lambdas sao funçoes sem nome, que podem ou nao receber parametros de entrada e retornar
valores.
'''
# Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programaçao em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui nao 

print(dicionario)