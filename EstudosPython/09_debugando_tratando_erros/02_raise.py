"""
Levantando os próprios erros com raise

raise -> Lança exeções 

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nosssas próprias exeções e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')



# Exemplo Real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O Texto {texto} será impresso na cor {cor}')

colore(True, 4)


def colore(texto, cor):
    cores = ('Verde', 'Amarelo', 'Azul', 'Branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O Texto {texto} será impresso na cor {cor}')

colore('Geek University', 'Preto')

OBS: O raise, assim como o return, finaliza a funçao. Ou seja, nada após o raise é executado.
"""
def colore(texto, cor):
    cores = ('Verde', 'Amarelo', 'Azul', 'Branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O Texto {texto} será impresso na cor {cor}')

colore('Geek University', 'Preto')