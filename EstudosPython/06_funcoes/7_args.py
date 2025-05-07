"""
Entendendo o *args

- O *args é um parametro, como outro qualquer. isto significa que voce poderá
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convençao, utilizamos *args para defini-lo

Mas o que é *args?

o parametro *args utilizado em uma funçao, coloca os valores extras informados como entrada
em uma tupla. entao desde já, lembre-se que tuplas sao imutáveis.



# Exemplos

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4


print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6, )) #TypeError

print(soma_todos_numeros(4, 6, 9, 5)) #TypeError





# Entendendo o args


#def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
#    return num1 + num2 + num3 + num4def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
#    return num1 + num2 + num3 + num4

def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros("Gabriel", "Gomes",))
print(soma_todos_numeros("Gabriel", "Gomes", 1))
print(soma_todos_numeros("Gabriel", "Gomes", 2, 3))
print(soma_todos_numeros("Gabriel", "Gomes",2, 3, 4))
print(soma_todos_numeros("Gabriel", "Gomes",3, 4, 5, 6))

print(soma_todos_numeros("Gabriel", "Gomes",23.4, 12.5))




# Outro exemplo de utilização do *args

def verifica_info(*args):
    if "Geek" in args and "University" in args:
        return "Bem-Vindo Geek!"
    return "Eu não tenho certeza quem voce é...."


print(verifica_info())
print(verifica_info(1, True, "University", "Geek"))
print(verifica_info(1, "University", 3.145))

"""

def soma_todos_numeros(*args):
    print(args)
    return sum(args)


#print(soma_todos_numeros())
#print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]


# Desempacotador 

print(soma_todos_numeros(*numeros))


# OBS: O asterisco serve para que informemos ao Python que estamos passando
# como argmuento uma coleçao de dados. Desta forma, ele saberá que precisará
# antes desempacotar estes dados.