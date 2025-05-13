"""
Decorators com diferentes asinaturas
    
# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern




# Relembrando 

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper() # Função .upper (deixa as letras caixa alta)
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'



@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# Testando

# print(saudacao('Angelina'))

print(ordenar('Picanha', 'Batata Frita'))



# Refatorando com o Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar 
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'
        

print(saudacao('Felicity'))

print(ordenar('Picanha', 'Batata Frita '))

@gritar
def lol():
    return 'lol'

print(lol())

# OBS: Vale lembrar que podemos utilizar parametros nomeados

print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

"""

# Decorator com argumentos 

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('Pizza')
def comida_favorita(*args):
    print(args)
    
    
@verifica_primeiro_argumento(10)
def soma_dez(num1, num2,):
    return num1 + num2


# Testando

print(soma_dez(10, 12)) # 22

print(soma_dez(1, 22)) # 22

print(comida_favorita('Pastel', 'Pizza'))