"""
POO - Propriedades - Properties

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes,
costumamos a criar métodos púlblicos para manipulação desses atributos. Esses métodos 
são conhecidos por getters e setters, onde os getters retornam o valor do atributo 
e os setters alteram o valor do mesmo.



class Conta:
    
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
        
#------------------------------------------#
    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def set_limite(self, limite): # Recebe um parâmetro e seta/altera o valor limite
        self.__limite = limite
#------------------------------------------#       

conta1 = Conta('Gabriel', 3000, 5000)
conta2 = Conta('Nayara', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Forma incorreta - É POSSÍVEL, MAS NUNCA É RECOMENDÁVEL FAZER UM ACESSO PRIVADO FORA DA CLASSE.
#soma = conta1._Conta__saldo + conta2._Conta__saldo


# Forma correta
soma = conta1.get_saldo() + conta2.get_saldo()

print(f'soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(9999999) 
print(conta1.__dict__)
"""
# 1 - Declarar classe
class Conta:
    
    # 2 - Atributo de classe
    contador = 0 
    
    # 3 construtor e seus atributos de Instância
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        
        
    # criando propriedade utilizando decorator - Consultas
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property 
    def limite(self): # essas property acima são padrão getter - conseguimos alterar
        return self.__limite
    
    @limite.setter  # setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
        
        
    # Métodos de Instância
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
        
    @property # não existe valor_total, estou criando agora, juntando o saldo + limite
    def valor_total(self):
        return self.__saldo + self.__limite
        
        
conta1 = Conta('Gabriel', 3000, 5000)
conta2 = Conta('Nayara', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo # conta1.'saldo' é nossa @property

print(f'a soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)

 # função tem parenteses, mas isso aqui não é uma função, é uma propriedade
#print(conta1.valor_total()) -> jeito errado

print(conta1.valor_total)
print(conta2.valor_total)
