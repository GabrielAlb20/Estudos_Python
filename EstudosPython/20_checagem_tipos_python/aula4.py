# Type Hinting

#def cumprimentar(nome: str) -> str: 
#    return f'Olá, {nome}'

#print(cumprimentar('Geek'))

#def cabecalho(texto, alinhamento=True):
#    if alinhamento:
#        return f"{texto.title()}\n{'-' * len(texto)}"
#    else:
#        return f" {texto.title()} ".center(50, '#')
    
    
#print(cabecalho('Geek University'))

#print(cabecalho('Geek University', alinhamento=False))


# Assim deixa o código mais legível, indicando o qual tipo deve receber.

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')
    
print(cabecalho('Geek University'))

print(cabecalho('Geek University', alinhamento=False))

print(cabecalho('Geek University', alinhamento='geek'))