"""
Listas Aninhadas  (Nested Lists)

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
      -Unidimensionais (Arrays/Vetores)
      - Multidimensionais (Matrizes)

Em Python nós temos as Listas

numeros = [1, 'b', 3.234, True, 5]


#print(listas) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(type(listas)) # <class 'list'>

# Como fazemos para acessar os elementos de uma lista aninhada?

#print(listas[0]) # [1, 2, 3]
#print(listas[0][1]) # 2
#print(listas[2][1]) # 8
    


# Exemplos
             #0         #1         #2
          #0  1  2    0  1  2    0  1  2
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3 

# Interando com loops em uma lista aninhada
for lista in listas:
    print(lista) # [1, 2, 3] [4, 5, 6] [7, 8, 9]
    for numero in lista:
        print(numero) # 1 2 3 4 5 6 7 8 9

# List Comprehension

[print(valor) for lista in listas for valor in lista] # 1 2 3 4 5 6 7 8 9

"""

# Outros exemplos

# Gerando um tabuleiro de xadrez/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha) 

# Gerando valores iniciais para o jogo da velha

velha = [['*' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)