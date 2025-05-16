'''
Conjuntos em Python

- Conjuntos em qualquer linguagem de programação estamos fazendo referencia a um conjunto matemático.
- Conjuntos são representados por {} ou set()
- Conjuntos são mutáveis, ou seja, podem ser alterados após a criação.

-sets (conjuntos) não possuem valores duplicados;
-sets (conjuntos) não possuem valores ordenados;
-Elementos não são acessados via índices, como em listas ou tuplas;
-sets (conjuntos) não suportam operações de fatiamento (slicing);
Aqui no Python, os conjuntos ~sao representados por {} ou set().
- Conjuntos não podem ter elementos duplicados, ou seja, se você tentar adicionar um elemento que já existe no conjunto, ele não será adicionado novamente.

- Conjuntos são mutáveis, ou seja, você pode adicionar ou remover elementos de um conjunto após sua criação.
- Conjuntos não suportam operações de fatiamento (slicing), ou seja, você não pode acessar elementos individuais de um conjunto como faria com listas ou tuplas.

Diferença entre Conjuntos (set) e Mapas (Dicionários) em Python:
        - Um dicionário tem chave/valor;
        - Um Conjunto tem apenas valor;

        


# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # REPARE QUE TEMOS VALORES REPETIDOS.
print(s)
print(type(s))

# OBS : Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo 
# será ignorado sem gerar error e não fará parte do conjunto.


# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type)

# Podemos verificar se determinado elemento está contido no conjunto 
if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')       
        
        
        
 # Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# dicionários não aceitam chaves duplicados, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')   


# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 23.22, 44}
print(s)
print(type(s))

# Podemos interar em um set normalmente

for valor in s:
    print(valor)
        
    

# Uso interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitante em uma feira ou museu. e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos.
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que voçê faria? Faria um lop na lista...?

# Podemos utilizar o set para isso:
print(len(set(cidades)))


# Adicionando elementos em um conjunto 
s.add(4)
s.add(4) # Duplicidade não gera erro. Simplismente é ignorado e não é adicionado.
print(s)


# Removendo elementos em um conjunto 
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3) # Não é índice! informamos o valor a ser removido

print(s)
# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. nenhum valor é retornado.


# Forma 2
s.discard(22)
print(s)
# OBS: Se o valor não for encontrado, nenhum erro é gerado.



# Copiando um conjunto para outro...

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)


# Forma 2 - Shallow Copy

novo = s 
 
novo.add(4)

print(novo)
print(s)


# Podemos remover todos os itens de um conjunto 

s.clear()
print(s)


# Precisamos gerar um conjunto com nomes de estudantes únicos.


 # Métodos Matemáticos de Conjuntos 

 # Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um 
 # contendo estudantes do curso de Java.
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme', }
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}


# Forma  1 - Utilizando union (Recurso da matemática/ União de dois conjuntos) - recomendado
unicos1 = estudantes_python.union(estudantes_java)
#unicos1 = estudantes_java.union(estudantes_python)
# {'Pedro', 'Guilherme', 'Gustavo', 'Ellen', 'Patricia', 'Ana', 'Fernando', 'Marcos', 'Julia'}
print(unicos1)



# Forma 2 - Utilizando o caractere pipe | 
unicos2 = estudantes_python | estudantes_java

print(unicos2)



# Veja que alguns alunos que estudam Python também estudam Java.

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection 

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando oo &

ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)




 '''

# Soma*, Valor Máximo*, Valor Minímo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
