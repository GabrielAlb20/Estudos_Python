"""
Lendo arquivos CSV

CSV - Comma Separared Values - Valores Separados por Vírgula

# Separador por vírgula

1, 2, 3, 4, 5, 6

'geek', 'university', 'python', 'ciencia', 'dados'



# separador por ponto e vírgula

1; 2; 3; 4; 5; 6

'geek'; 'university'; 'python'; 'ciencia; 'dados'



# separador por espaço

1 2 3 4 5 6

'geek' 'university' 'python' 'ciencia' 'dados'


# Possível de se trabalhar, mas nao é o ideal - trabalhoso
#with open('lutadores.csv') as arquivo:
   # dados = arquivo.read()
    #print(type(arquivo))
   # dados = dados.split(' ,')
  #  print(dados)


A linguagem Python, possui duas formas diferentes para ler dados em arquivos CSV:
    -reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    -DictReader -> permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts:



    # Reader 


import csv

try:
    with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            print(linha)
except UnicodeDecodeError as e:
    print(f"Erro de decodificação Unicode: {e}")
    print("Tente abrir o arquivo com uma codificação diferente.")
    print("Possíveis codificações: 'latin-1', 'cp1252', etc.")
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome do arquivo e o caminho.")


from csv import reader

with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    print(type(leitor_csv))
    next(leitor_csv) # Pula o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros')


        

# DictReader

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} ")

"""


# DictReader com outro separador

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=';')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} ")


