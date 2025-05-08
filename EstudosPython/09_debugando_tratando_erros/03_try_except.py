'''
o block try/except

Utilizamos o bloco try/execpt para tratar erros que podem ocorrer no nosso código. previnindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try: 
    //execução problemática
except:
    // o que deve ser feito em caso de problema

'''

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
# except:/
    print('Deu algum problema')


# PAUSANDO NA 7:00