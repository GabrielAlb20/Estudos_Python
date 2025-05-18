""""
Trabalhando com deltas de data e hora

data_inicial == dd/mm/yyyy 12:55:34.9393999
data_final == dd/mm/yyyy   16:48:27.6789090

delta = data_final - data_inicial


import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2026, 3, 3, 0)

# Calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(tempo_para_evento.days)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas..')



import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
"""


import datetime

data_hoje = datetime.datetime.now()

data_nasc_vo = datetime.datetime(1915, 2, 1, 0, 0)  # Criando um objeto datetime para a data de nascimento

idade_se_vivo = data_hoje - data_nasc_vo

print(idade_se_vivo)