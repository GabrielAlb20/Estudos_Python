"""Conceitos Básicos e Sintaxe"""

# Este é um comentário de linha única

'''
Este é um comentário de múltiplas linhas.
Ele pode ser usado para explicar blocos de código mais longos.
'''

# Exemplo de impressão no console
print("Olá, Mundo!")


# Variáveis

# Definindo variáveis
nome = "Gabriel"
idade = 20
altura = 1.75

# Exibindo o conteúdo das variáveis
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)



# Tipos De Dados

# Tipos de dados básicos
nome = "Maria"  # string
idade = 30  # inteiro
altura = 1.68  # float
eh_maior_de_idade = True  # booleano

# Exibindo os tipos de dados
print(type(nome))  # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(altura))  # <class 'float'>
print(type(eh_maior_de_idade))  # <class 'bool'>


# Entrada de Dados

# Solicitando ao usuário para inserir dados
nome_usuario = input("Qual é o seu nome? ")
idade_usuario = int(input("Quantos anos você tem? "))

# Exibindo os dados inseridos pelo usuário
print("Olá,", nome_usuario)
print("Você tem", idade_usuario, "anos.")



# Saída de Dados (Formatada)

# Exibindo uma mensagem formatada
nome = "Carlos"
idade = 28
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Utilizando .format() para formatação
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))
