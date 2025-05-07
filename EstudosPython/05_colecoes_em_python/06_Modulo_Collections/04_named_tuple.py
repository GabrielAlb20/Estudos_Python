'''
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1, 2, 3)
print(tupla[1])


Named Tuple -> Sao tuplas, diferenciadas, onde, especificamos um nome para a mesa e também parametros

'''
# Importando 

from collections import namedtuple

# Precisamos definir o nome e os parametros

# Forma 1 - Declaraçao Named Tuple

cachorro = namedtuple('Cachorro', 'Idade raca nome')


# Forma 2 = Namede Tuple

cachorro = namedtuple('Cachorro', 'idade, raca, nome')

# Forma 3 - Declaraçao Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca ='Chow-Chow', nome= 'Ray')

print(ray)

print(ray[0]) # Idade
print(ray[1]) # Raça
print(ray[2]) # nome

# Forma 2
print(ray.idade) # Idade
print(ray.raca) # Raça
print(ray.nome) # Nome

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
