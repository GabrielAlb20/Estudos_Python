"""
Reduce 

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). agora temos que
importar e utilizar a oartir do módulo 'functools'.


Guido van Rossun: Utilize a função reduce() se você realmente precisar dela. Em todo caso, 99% das vezes um loop for é mais legível e mais fácil de entender.


Para entender o reduce()

# Imagine que voce tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E voce tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

    
assim como map() e filter(), a função reduce() também recebe dois parametros: a função e o iterável.

reduce(funcao, dados)


A função reduce(), funciona da seguinte forma:
  Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e retorna o resultado.
  Passo 2: res2 = f(res1, a3) # Aplica a função no resultado do passo 1 e no próximo elemento da coleção e retorna o resultado.

Isso é repetido até o final da coleção.
Passo 3: res3 = f(res2, a4) 
.
.
.
Passo n: resn = f(resn-1, an) # Aplica a função no resultado do passo n-1 e no próximo elemento da coleção e retorna o resultado.

Ou seja em cada passo ela aplica a função no resultado do passo anterior e no próximo elemento da coleção.
# No final, a função reduce() retorna o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ..., an)
# Ou seja, ela aplica a função em todos os elementos da coleção e retorna o resultado final.

"""

# Como funciona na prática:

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista.

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar a função reduce(), precisamos de uma função que receba dois parâmetros.
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)  # 25878772920
# OBS: Assim como nas funções map() e filter(), após serem utilizados os dados de reduce(), eles são excluídos da memória.


# Utilizando um loop normal
res = 1
for n in dados:
    res = res * n

print(res)  # 25878772920