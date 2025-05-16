"""
POO - O método super()

O método super() se refere á super classe.


"""

# Vamos relembrar
# classe animal com 2 atributos privados: nome e especie
class Animal: # classe pai
    # método init
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie
    
    # método recebe parametro e imprime algo
    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal): # classe filha, classe que herdam de outras classes
    
    # construtor
    
    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie) # consultor da classe pai - possivel, mas não é legal.
        super().__init__(nome, especie) # recomendado
        super().faz_som('auauauauau') # com o método super, podemos acessar qualquer elemento da classe pai, atributos e métodos
        self.__raca = raca
        
felix = Gato('Felix', 'Felino', 'Angorá')

felix.faz_som('miau')

