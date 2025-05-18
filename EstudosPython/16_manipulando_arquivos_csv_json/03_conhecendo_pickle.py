""""
Conhecendo o Pickle


Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

#OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma
não é recomendado trabalhar com arquivos pickle vindos de outras pessoas
que voce não conheça ou de fontes desconhecidas.

# Fazendo a escrita em arquivos pickle

felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.piclke', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.nome} está comendo')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def mia(self):
        print(f'{self.nome} está miando...')

    
class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def late(self):
        print(f'{self.nome} está latindo...')


# Fazendo a leitura de dados em arquivos pickle

with open('animais.piclke', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')


    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do gato é {type(cachorro)}')