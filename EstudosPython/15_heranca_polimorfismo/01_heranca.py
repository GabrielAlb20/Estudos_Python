"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.


Cliente
    - nome;
    - sobrenom;
    - cpf;
    - renda;
    
Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;
    
Perguntar: Existe alguma entidade genérica o suficiente para encapsular os atributos 
e métodos comuns a outras entidades?



class Cliente:
    
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda
        
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
class Funcionario:
    
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula
        
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    

cliente1 = Cliente('Nayara', 'Albuquerque', '123.456.789.-00', 5000)
funcionario1 = Funcionario('Gabriel', 'Albuquerque', '989.756.432-00', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# OBS: Quando uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;
    
Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;
    
    
    
    
class Pessoa: # Classe Genérica - Forma mais Genérica, pra ser um funcionário/cliente tem que ser uma Pessoa.
    
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    #Cliente herda de Pessoa
    
    def __init__(self, nome, sobrenome, cpf, renda):
        #Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        super().__init__(nome, sobrenome, cpf)   # SUPER CLASSE -> Forma recomendada
        self.__renda = renda
        
        
class Funcionario(Pessoa):
    #Funcionario herda de Pessoa
    
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)   # SUPER CLASSE: -> Forma recomendada
        self.__matricula = matricula


cliente1 = Cliente('Gabriel', 'Albuquerque', '123.456.789.-00', 5000)
funcionario1 = Funcionario('Nayara', 'Albuquerque', '989.756.432-00', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)

print(funcionario1.__dict__)


# Sobrescrita de Métodos (Overriding)

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super classe 
em classes filhas.
"""


class Pessoa: # Classe Genérica - Forma mais Genérica, pra ser um funcionário/cliente tem que ser uma Pessoa.
    
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    
    def __init__(self, nome, sobrenome, cpf, renda):
        #Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        super().__init__(nome, sobrenome, cpf)   # SUPER CLASSE -> Forma recomendada
        self.__renda = renda
        
class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)   # SUPER CLASSE: -> Forma recomendada
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(super._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'

# Exemplo que nem é sempre possivel a herança
class Pinguim(Pessoa): # Pinguim não é uma Pessoa.
    
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome
        

cliente1 = Cliente('Gabriel', 'Albuquerque', '123.456.789.-00', 5000)
funcionario1 = Funcionario('Nayara', 'Albuquerque', '989.756.432-00', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
