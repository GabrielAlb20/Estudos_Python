"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.

"""
"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.

"""
# MINHA VERSÃO, ADICIONEI MAIS DETALHES SOBRE A 'PESSOA'
class Pessoa:
    
    def __init__(self, nome, sobrenome, data_nascimento, email, idade, altura, peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.idade = idade
        self.altura = altura
        self.peso = peso

pessoa1 = Pessoa('Gabriel', 'Gomes', '05/06/2004', 'gabrielgomes@gmail.com', 20, 1.65, 62)

print(f'o nome da pessoa é: {pessoa1.nome}')
print(f'o sobrenome: {pessoa1.sobrenome}')
print(f'a data de nascimento é: {pessoa1.data_nascimento}')
print(f'o email é: {pessoa1.email}')
print(f'a idade é: {pessoa1.idade}')
print(f'a altura é: {pessoa1.altura}')
print(f'e o peso é: {pessoa1.peso}')

# VERSÃO/REVISÃO DO EXERCICIO UDEMY