"""
Documentando funções com Docstring

OBS: Podemos ter acesso a documentação de uma função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso á documentaçao ocm a funçao help()
"""

# Exemplos 

def diz_oi():
    """uma função simples que retorna a string 'Oi!'"""
    return "Oi!"


print(diz_oi())
print(help(diz_oi))

print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Funçao que retorna por padrao o quadrado de 'numero' ou 'numero' á 'potencia' informada.
    param numero: Número que desejamos gerar o exponencial.
    param potencia: Potencia que queremos gerar o exponencial. por padrao é 2
    return: retorna o exponencial de 'número' por 'potencia'.

    """
    return numero ** potencia
