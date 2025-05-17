"""
POO - Herança Múltipla 


Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, 
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas 

#OBS: A herança múltippla pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivaçao Indireta;


# Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivaçao Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass
    

#OBS: não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará 
todos os atributos e métodos da super classe.
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'
    

class Terrestre(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)
   
    def andar(self):
        return f'{self._Animal__nome} está andando'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)



# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) # Eu sou Tux da terra! / Eu sou Tux do mar!  - Method Resoluton Order - MRO



# Objeto é instancia de...

print(f'Tux é instancia de Pinguim? {isinstance(tux, Pinguim)}') # True
print(f'Tux é instancia de Aquático? {isinstance(tux, Aquatico)}') # True
print(f'Tux é instancia de Terrestre? {isinstance(tux, Terrestre)}') # True
print(f'Tux é instancia de Animal? {isinstance(tux, Animal)}') # True 
print(f'Tux é instancia de object? {isinstance(tux, object)}') # True
