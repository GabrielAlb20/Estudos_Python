""""
Métodos de Data e Hora



# Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now() # now == agora
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.date.today() # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))



# Mudanças ocorrendo á meia-noite

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))




import datetime

# Encontrar o dia da semana. weekday()

# Os dias da semana do método weekday() começam em 0, sendo esta a segunda-feira

# 0 - Segunda-feira (Monday)
# 1 - Terça-feira (Tuesday)
# 2 - Quarta-feira (Wednesday)
# 3 - Quinta-feira (Thursday)
# 4 - Sexta-feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo(Sunday)


import datetime

aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Voce nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Voce nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Voce nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Voce nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Voce nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Voce nasceu em um sábado')
elif aniversario.weekday() == 6:
    print('Voce nasceu em um domingo')



def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'

        


import datetime
from deep_translator import GoogleTranslator


def formata_data(data):
    return f"{data.day} de {GoogleTranslator(source='en', target='pt').translate(data.strftime('%B'))} de {data.year}"


hoje = datetime.datetime.today()
print(formata_data(hoje))



import datetime
from deep_translator import GoogleTranslator
 
 
def formata_data(data):
    # GoogleTranslator -> É uma classe que converte idiomas.
    # param source='en' -> Idioma que se encontra a string.
    # param target='pt' -> O idioma a ser convertido a mensagem.
    # método translate() da classe GoogleTranslator -> Recebe somente
    # o dado a ser traduzido.
    
    tradutor = GoogleTranslator(source="en", target="pt")
    return f"{data.day} de {tradutor.translate(data.strftime('%B'))} de {data.year}"
 
 
hoje = datetime.datetime.today()
print(formata_data(hoje))


# Somente a hora

almoco = datetime.time(12, 30, 0)

print(almoco)



import timeit

# Marcando tempo de execução do nosso código com timeit

# Loop for
tempo_for = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Tempo com loop for: {tempo_for:.6f} segundos")

# List Comprehension
tempo_comprehension = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(f"Tempo com list comprehension: {tempo_comprehension:.6f} segundos")

# Map
tempo_map = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(f"Tempo com map: {tempo_map:.6f} segundos")



"""

import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000)) # 5.281697099999292