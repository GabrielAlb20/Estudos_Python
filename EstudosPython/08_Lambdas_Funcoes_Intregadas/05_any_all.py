"""
Any e All

all() -> Retorna True se todos os elementos do iterável forem verdadeiros ou se o iterável estiver vazio.



# Exemplo 1 - all()

print(all([1, 2, 3, 4, 5]))  # Todos os números são verdadeiros, então retorna True
print(all([1, 2, 3, 4, 5, 0]))  # Um número é falso (0), então retorna False
print(all([])) # Todos os números são verdadeiros? True
print(all((1, 2, 3, 4, 5,))) # Todos os números são verdadeiros? True
print(all({1, 2, 3, 4, 5,})) # Todos os números são verdadeiros? True
print(all('Geek')) # Todos os números são verdadeiros? True



nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina',]

print(all([nome[0] == 'C' for nome in nomes]))


# OBS: Um interável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all(num for num in [4, 2, 10, 6, 8] if num % 2 == 0))


any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""
print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, (), []])) # False (se todos forem falsos, retornará False, se houver 1 verdadeiro, retornará True.)

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))