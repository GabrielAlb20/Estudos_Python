"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anônimas, que podem ter qualquer número de argumentos, mas apenas uma expressão.



# Função em Python

def funcao(x):
    return 3 * x + 1


print(funcao(4)) # 13
print(funcao(5)) # 16
print(funcao(6)) # 19
print(funcao(1)) # 4

# Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda?

calc = lambda x: 3 * x + 1

print(calc(4)) # 13
print(calc(5)) # 16 



# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo('  FELICITY       ', 'jones'))

# Em funçoes Python Podemos ter nenhuma ou várias entradas. Em Lambdas também

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z:3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn: <expressão>

print(amar()) # Como não amar Python?
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))


# OBS: Se passarmos mais argumentos do que parametros esperados  teremos TypeError


"""

# Outro exemplo

autores = ['Issac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)