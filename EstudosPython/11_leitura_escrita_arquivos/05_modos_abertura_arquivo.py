''''
Modos de abertura de Arquivo

r -> Abre para leitura - Padrão
W -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir
'''

with open('university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo.\n')
    