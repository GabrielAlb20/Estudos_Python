# Checagem de Tipos com MyPy
# pip install mypy
# Checa se está tudo correto, tipos...

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')
    
    
print(cabecalho('Geek University'))

print(cabecalho('Geek University', alinhamento=False))

print(cabecalho('Geek University', alinhamento=True))

cabecalho(texto=4, alinhamento=8)

# Correto

texto: str

# Incorreto

texto:str

texto : str

# Correto

alinhamento: bool = True

# Incorreto

alinhamento:bool=True

alinhamento: bool = True

alinhamento: bool=True

alinhamento: bool= True

