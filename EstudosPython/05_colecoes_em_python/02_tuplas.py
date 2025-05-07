'''
listas em python funcional como vetores/matries (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar qualquer tipo de dado.

Linguagens C/Java: Arrays
        - possuem tamanho e tipo de dado fixo;
        ou seja, nestas linguagens se voce criar um array do tipo int e com tamanho 5, esse array
        será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

    já em Python:
    
        
        - Dinâmico: não possui tamanho fixo; ou seja, podemos criar a lista e simplismente ir adicioando elementos;
        - qualquer tipo de dado: não possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado;

    As listas em python são representadas por colchetes: []
    
        python roda em várias máquinas hardware, notebook, celulares, desktop, super computadores, a memória ram vai preenchendo de acordo 
        com a quantidade de informações que são armazenadas .

        dir = vai listar todos os métodos que podem ser aplicados a lista (outros dados)
        help = vai mostrar o que cada método faz e como usar.

'''

lista1 = [1, 2, 3, 4, 5, 27, 40, 99, 54, 20, 43]
lista2 = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
lista3 = []
lista4 = list(range(11))
lista5 = list('Gabriel')

# podemos facilmente checar se determinado elemento existe na lista:

num = 7
if num in lista1:
    print(f'O número {num} existe na lista 1')
else:
    print(f'O número {num} não existe na lista 1')

# podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

# podemos facilmente contar o numero de ocorrencias de um valor em uma lista

print(lista1.count(1))
print(lista1.count(2))
print(lista2.count('G'))


# adicionar elementos a lista
'''
PARA ADICIONAR ELEMENTROS A LISTA, UTILIZAMOS A FUNÇÃO append() OU A FUNÇÃO insert()

'''
print(lista1)
lista1.append(42)# adifionar o elemento 42 ao final da lista
print(lista1)
lista1.insert(0, 100)# adicionar o elemento 100 na posição 0 da lista
print(lista1)

# Com append, nós só conseguimos adicionar 1 elemento por vez, já com o insert, nós conseguimos adicionar mais de um elemento por vez.
#
# Exemplo:
# lista1.insert(0, 100, 200, 300) # isso não funciona
# lista1.append(100, 200, 300) # isso também não funciona

lista1.append([8, 3, 2]) # isso funciona, mas adiciona a lista como um elemento só 'colocando a lista como elemento único (sublista)
print(lista1)

if [22, 22, 22] in lista1:
    print('A lista [8, 3, 2] existe na lista1')
else:
    print('não encontrei [8, 3, 2] na lista1')

lista1.extend([8, 3, 2]) # isso funciona, mas adiciona a lista como um elemento só 'coloca cada elemento da lista como valor á lista
print(lista1)

lista1.extend('Gabriel') # isso funciona, mas adiciona a lista como um elemento só 'coloca cada elemento da lista como valor á lista
print(lista1)


# não existem limitações para tipos de dados

