"""
Funções com Parametro Padrao (Default Paramters)

- Funções onde a passagem de parametro seja opcional;

# Exemplo de função onde a passagem de parametro seja opcional
print('Geek University')

print()

# Exemplo de funçao onde a passagem de parametro seja obrigatória 
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError



def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva a potencia informada pelo usuario

# Obs: 
# Se o usuário passar somente 1 argumento, este será atribuido ao parametro numero, e será calculado o quadrado desde número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parametro numero e o segundo ao parametro potencia. Então será calculada esta potencia

print(exponencial())



# OBS: Em funçoes Python, os parametros com valores dafault (padrao ) DEVEM sempre estar ao final da declaraçao.

# ERRO!
def teste(num=2, potencia):
    return num ** potencia

print(teste(6))


# Outros exemplos

def soma(num1, num2): # Se eu setar os valores aqui, ele substitui
    return num1 + num2

print(soma(4, 3))
print(soma(4)) # TypeError
print(soma()) # TypeError



# Exemplo mais complexo 

def mostra_informacao(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return "Bem-vindo instrutor Geek!"
    elif nome == "Geek":
        return"Eu pensei que voce era o instrutor"
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(True))
print(mostra_informacao(nome='Stephany'))


# Por que utilizar parametros com valor default?

- Nos permite ser mais flexiveis nas funçoes;
- Evite erros com parametros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;'


# Quais tipos de dados podemos utilizar com valores default para parametros?
 - Qualquer tipo de dado:
    - Numeros, strings, floats, booleanos, listas, tuplas, dicionarios, funcoes e etc;


# Exemplos

def soma(num1, num2):
    return num1+ num2
def mat(num1, num2, fun=soma):
    return fun(num1, num2)
def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo - Evitar problemas e confusoes..

# Variáveis globais
# Variáveis locais

instrutor = "Geek" # Variavel Global

def diz_oi():
    instrutor = 'Python' # Variável Local
    return f'Oi {instrutor}'

print(diz_oi())

#OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferencia

def diz_oi():
    prof = 'Geek' # Variavel local
    return f'Olá {prof}'

print(diz_oi())

print(prof) # NameError


total = 0 

def incrementa():
    total = total + 1 # UnboundLocalError (A variável local está seundo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())

# ATENÇAO com variáveis globais (Se puder evitar, evite!)

total = 0 

def incrementa():
    global total # Avisando que queremos utilizar a variável global

    total = total + 1 
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""