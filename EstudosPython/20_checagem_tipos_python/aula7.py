"""
# Checagem de Tipos com MyPy
# pip install mypy
# Checa se está tudo correto, tipos...

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')
    
    
print(cabecalho('Geek University'))

print(cabecalho('Geek University', alinhamento=False))

print(cabecalho('Geek University', alinhamento=True))

cabecalho(texto=4, alinhamento=8)

# Correto

texto: str

# Incorreto

texto:str

texto : str

# Correto

alinhamento: bool = True

# Incorreto

alinhamento:bool=True

alinhamento: bool = True

alinhamento: bool=True

alinhamento: bool= True




# print(circunferencia.__annotations__) # Retorna um dicionário

nome: str = 'Geek University'

peso: float = 67.9

ativo: bool = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)
"""

import math
def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

class Pessoa:
    
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        
    def andar(self) -> str:
        return f'{self.__nome} está andando'
    
p = Pessoa(nome='Geek University', idade=37, peso=69.5)

print(p.__dict__)
#print(type(p))

#print(p.__annotations__) Não tem annotations

print(p.andar.__annotations__)

print(p.__init__.__annotations__)