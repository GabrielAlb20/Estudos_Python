"""
Set Comprehension


# Pense no seguinte:
Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}


"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros) # {1, 2, 3, 4, 5, 6}

# Outro exemplo

numero = {x ** 2 for x in range(10)}
print(numero) # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# DESAFIO! Faça uma alteração na estrutura na estrutura acima para gerar um dicionário
# ao invés de um set. O resultado deve ser o mesmo, mas a estrutura deve ser diferente.

numero = {x:x ** 2 for x in range(10)}
print(numero) # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Pra finalizar

letras = {letra for letra in 'Geek University'}
print(letras) # {'G', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'r', 's', 't', 'y'}
