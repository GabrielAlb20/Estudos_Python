'''
Erros mais comuns em Python 

ATENÇAO: É importante prestar atençao e aprender a ler as saídas de erros geradas pela execuçao

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou Seja, voce escreveu algo que o Python
nao reconhece como parte da linguagem


Exemplos SyntaxError

a)

def funcao:
    print('Geek University')

    
b)

None = 1
def = 1


c)

return




2 - NameError -> Ocorre quando uma variável  ou funçao nao foi definida.

a)

print(geek)

b)
geek()

c)

a = 18
msg = ''
if a < 10:
    msg = 'É Maior que 10'

print(msg)


3 - TypeError -> Ocorre quando uma funçao/operaçao/açao é aplicada a um tipo errado.'
 
 Exemplos TypeError

a) 
print(len(5))

b)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado 

a)

lista = ['Geek']
print(lista[2])

b)

lista = ['Geek']
print(lista[0][10])

c)

tupla = ('Geek')
print(tupla[0][10])


5 - ValueError -> Ocorre uma funçao/operaçao built-in (integrada) recebe um argumento com tipo correto
mas tipo inapropriado.

a)

print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que nao existe.

a)

dic = {}
print(dic['geek'])


7 - AttributeError -> Ocorre quando uma variável nao tem um atributo/funçao.

Exemplos AttributeError

a)

tupla = (11, 2, 31, 4)

print(tupla.sort())


8 - IdentatationError ->  Ocorre quando não respeitamos a identaçao do Python (4 espaços)

Exemplos IdentationError

a)

def nova():
print('Geek')

b)

for i in range(10):
i + 1

OBS: Exceptions e Erros sao sinonimos na programaçao.

OBS: Importante ler e prestar atençao na saída de erro.
'''





