"""
Try / Except / Else / Finally 

Dica de quando e onde tratar código:

TODA ENTRADA DO USUÁRIO DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.


# Else -> É executado soment se não ocorrer o erro.

try:
    num = int(input("Informe um número: "))
except ValueError:
    print('Valor incorreto')
else:
    print(f"Você digitou {num}")


    
# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou um número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente é utilizado para fechar ou desalocar recursos.




# Exemplo mais complexo CORRETO
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print('Valor incorreto')
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


# Exemplo mais complexo CORRETO - Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

"""


# Exemplo mais complexo CORRETO - Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return (f'Ocorreu um problema: {err}')

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))





