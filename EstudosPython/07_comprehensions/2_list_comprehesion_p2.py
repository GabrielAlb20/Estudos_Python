"""
List Comprehension - Parte 2

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehensions,


"""

# Exemplos

#1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numeros for numeros in numeros if numeros % 2 == 0]
impares = [numeros for numeros in numeros if numeros % 2 != 0]

print(pares)
print(impares)


# Refatorar
# Qualquer número par módulo de 2 é 0, e 0 em Python é considerado False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualque número ímpar módulo de 2 é 1, e 1 em Python é considerado True. not True = False
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)