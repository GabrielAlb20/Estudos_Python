"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamada datetime


2025-05-18 15:04:47.632982

2025-05-18 15:08:47.632982



import datetime

#print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)


# Retorna a data e hora corrente
print(datetime.datetime.now()) # 2025-05-18 14:59:57.104474     BR 18/05/2025

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora


inicion = datetime.datetime.now()

print(inicion)

# Alterar o horário para 16 horas, 0 minutos, 0 segundo, 0 microsegundo
inicio = inicion.replace(year=2030, hour=16, minute=0, second=0, microsecond=0)

print(inicio)



import datetime

evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))

print(type('31/12/2018'))

print(evento)



nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))

# Recebendo dados do usuário e convertendo para data



"""

import datetime

evento = datetime.datetime.now()

# Acessa individual dos elementos de data e hora

print(evento.year) # Ano
print(evento.month) # Mes
print(evento.day) # Dia
print(evento.hour) # Hora
print(evento.minute) # Minuto
print(evento.second) # Segundo
print(evento.microsecond) # Microsegundo

print(dir(evento))