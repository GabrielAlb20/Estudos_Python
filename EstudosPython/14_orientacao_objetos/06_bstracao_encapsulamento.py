"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando
classes.

Encapsular -> cápsula


           classe 
 ____________________________
|                            |
|    Atributos e métodos     |
|                            |
|____________________________|

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas, Python não bloqueia esse acesso 
fora da classe. Com Python acontece um fenômeno chamado
Name Mangling, que faz uma alteração na fora de se acessar
os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

# SE FOSSE UM MÉTODO

instancia._Pessoa__fala()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.


print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular) # Name Mangling (ERRADO)

conta1._Conta__titular = 'Angelina'

print(conta1.__dict__)



conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(10)

print(conta1.__dict__)


"""


"""class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

meu_carro = Carro("Sedan", "Azul")
print(meu_carro.modelo)  # Acesso direto ao atributo público
meu_carro.cor = "Vermelho" # Modificação direta do atributo público
print(meu_carro.cor)


class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo  # Convenção de atributo protegido

    def exibir_saldo(self):
        print(f"Saldo: R${self._saldo:.2f}")

minha_conta = ContaBancaria(1000)
minha_conta.exibir_saldo()
print(minha_conta._saldo) # Ainda é possível acessar diretamente (mas não é recomendado!)
minha_conta._saldo = -50 # Também é possível modificar diretamente (e é uma má prática!)
minha_conta.exibir_saldo()


class Livro:
    def __init__(self, titulo, __numero_paginas):
        self.titulo = titulo
        self.__numero_paginas = __numero_paginas # Convenção de atributo privado

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Páginas: {self.__numero_paginas}")

meu_livro = Livro("Dom Quixote", 800)
meu_livro.exibir_detalhes()
#print(meu_livro.titulo) # Acesso público funciona

# print(meu_livro.__numero_paginas) # Isso geraria um AttributeError!

# Para acessar (com cuidado), você usaria o "name mangling":
print(meu_livro._Livro__numero_paginas)
"""
class Conta:

    contador = 400
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')
        
    def depositar(self, valor):
        if valor > 0:  
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
    
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor  
            else:
               print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')
    
    def transferir(self, valor, conta_destino):
        # 1 - Remover valor da conta de origem 
        self.__saldo -= valor
        self.__saldo -= 10 # Taxa de transfêrencia paga por quem realizou a transfência
        
        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor
        
            
# Testando 
conta1 = Conta('Gabriel', 150.0, 1500)
conta1.extrato()

conta2 = Conta('Nayara', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()