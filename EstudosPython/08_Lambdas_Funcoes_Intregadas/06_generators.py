"""
Generators Expression

Em aulas anteriores nós estudamos:
- List Comprehesion;
- Dictionary Comprehension;
- Set Comprehesion;

Não vimos:
- Tuple Comprehension... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print([nome[0] = == 'C' for nome in nomes])



# Poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))


# List Comprehesion
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)
# Generator (O mais rápido, ocupa menos recursos na memória)
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)


# Qual é a utilizade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parametro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaços ocupa.
print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(92345668823))
print(getsizeof(True))



from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dicionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dicionary Comprehension:{dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')
"""

# Eu posso interar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)