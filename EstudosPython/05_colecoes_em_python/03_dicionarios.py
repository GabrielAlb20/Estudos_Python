'''
Dicionários em Python

OBS: Em algumas linguagens de programação, os dicinoários são chamados de mapas ou tabelas hash.
Dicionários são mutáveis, ou seja, podem ser alterados após a criação.


Dicionários são estruturas de dados que armazenam pares de chave-valor.

Dicionários são representados por {}.
print(type({}))

# OBS: Sobre dicionários
  - Chave e valor são separados por dois pontos (:);
  - Tanto chave quanto valor podem ser de qualquer tipo de dado;
  - Podemos misturar tipos de dados;

# Criando dicionários
# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'EUA': 'Estados Unidos', 'Py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menso comum)

paises = dict(br='Brasil', EUA='Estados Unidos', Py ='Paraguai')
print(paises)
print(type(paises))
  
paises = {'br': 'Brasil', 'EUA': 'Estados Unidos', 'Py': 'Paraguai'}

# Acessando elementos 

# Forma 1 - Acessando via chava, da mesma forma que lista/tupla
print(paises['br'])
print(paises['EUA'])
#print(paises['ru']) # KeyError: 'ru' - Chave não existe no dicionário

# OBS: Se a chave não existir, o Python retorna um erro (KeyError).

# Forma 2 - Acessando via get() - Recomendada

print(paises.get('br'))
print(paises.get('ru')) # None - Retorna None se a chave não existir

# Caso o get nao encontre o objeto com a chave informada, será retornado o valor None e não será
gerado KeyError

pais = pais.get('ru') # None - Retorna None se a chave não existir

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para o caso de não encontrar a chave no dicionário

pais = paises.get('ru', 'Não encontrado')
print(pais) # Não encontrado

# Podemos verificar se determinada chave se encontra em um dicionário 

print('br' in paises) # True - A chave existe no dicionário
print('ru' in paises) # False - A chave não existe no dicionário
print('Estados Unidos' in paises) # False - O valor não existe no dicionário

if 'ru' in paises:
    russia = paises['ru']

    
# Podemos utilizar qualquer tipo de dado (int, float, str, list, tuple, set, dict) como chave
# de dicionários.

# Tuplas(IMUTÁVEL) por exemplo são bastante interessantes de serem utilizadas como chaves de dicionários,
# pois as mesmas são imutáveis e não podem ser alteradas após a criação.
localicades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova Iorque',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localicades)
print(type(localicades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - Mais comum - Adicionando um novo elemento

receita['abr'] = 500
print(receita)

# Forma 2 - update() - Atualiza o dicionário com os elementos do outro dicionário
# ou adiciona novos elementos.
# Se o elemento já existir, ele será atualizado.
# Se o elemento não existir, ele será adicionado.  

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário

# Forma 1 - 

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionário, NÃO podemos ter chaves repetidas.

# Se tentarmos adicionar um novo elemento com uma chave que já existe, o Python irá sobrescrever o valor
# existente.

# Remover dados de um dicionário 

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# forma 1 - Mais utilizada
ret = receita.pop('mar') # pop remove o ultimo elemento do dicionário e retorna o valor removido.
print(ret)

print(receita)
# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2 

del receita['fev']

print(receita)
# OBS: Aqui também precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS: O del não retorna o valor removido.

# Imagine que você tem um comércio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.


Carrinhos de compras:
    Produto 1:
      - nome;
      - quantidade;
      - preço;

    Produto 2:
      - nome;
      - quantidade;
      - preço;


# 1 - Poderíamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Playstation 5', 1, 2300.00]
produto2 = ['God of War 4', 1,  150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 5', 1, 2300.00)
produto2 = ('God of War 4', 1,  150.00)

carrinho = (produto1, produto2)

print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderiamos utilizar um Dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 5', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)   

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos acessar as informações através de chaves, como por exemplo:
# produto1['nome'], produto1['quantidade'] e produto1['preco'].
# Agora temos um dicionário com chaves e valores, onde podemos acessar os valores através das chaves.

# Limpar o dicionário (Zerar dados)


# Copiando um dicionário para outor
# Forma 1 # Deep Copy

novo = d.copy() # Copia o dicionário d para o dicionário novo
print(novo)

novo['d']  = 4 # Adicionando um novo elemento no dicionário novo

print(d) # {'a': 1, 'b': 2, 'c': 3}
print(novo) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# OBS: O dicionário d não foi alterado, pois o mesmo foi copiado para o dicionário novo.



# Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))


# Forma 2 # Shallow Copy

novo = d # Copia o dicionário d para o dicionário novo
print(novo)

novo['d']  = 4 # Adicionando um novo elemento no dicionário novo
print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(novo) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# OBS: O dicionário d foi alterado, pois o mesmo foi copiado para o dicionário novo.








'''

# Forma não usual de criação dicionários

outro = {}.fromkeys('a', 'b')

print(outro) # {'a': 'b'}
print(type(outro)) # <class 'dict'>
# OBS: O fromkeys cria um dicionário com as chaves informadas e o valor informado.

usuario = {}.fromkeys(['nome', 'pontos', 'email'], 'desconhecido')
print(usuario) # {'nome': 'desconhecido', 'idade': 'desconhecido', 'email': 'desconhecido'}
print(type(usuario)) # <class 'dict'>

# o método fromkeys recebe dois parâmetros:
# 1 - Uma lista com as chaves do dicionário
# 2 - Um valor padrão para todas as chaves do dicionário.

veja = {}.fromkeys('teste', 'valor')
print(veja) # {'t': 'valor', 'e': 'valor', 's': 'valor'}
print(type(veja)) # <class 'dict'>


veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)