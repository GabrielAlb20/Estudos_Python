"""
Map

Com map, fazemos mapeamento de valores para função.



import math
# Exemplo de uso do map com uma função que calcula a raiz quadrada de um número

def area(r):
    Calcula a área de um círculo com raio 'r' 
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma com map
# Map é uma função que recebe dois parâmetros: O primeiro é a função que queremos aplicar e o segundo é o iterável. Retorna um Map Object.

areas = map(area, raios)


print(areas)
print(type(areas))

print(list(areas))  # <map object at 0x7f8c1c2e3d90>


# Forma 3 - Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map(), depois da primeira utilização do resultado, ele zera.


#Para fixar - Map

# Temos dados interáveis:

# dados: a1, a2, ..., an

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# o Map Object: f(a1), f(a2), ..., f(an)
# O resultado do map é um Map Object, que é um iterável, ou seja, podemos utilizar o for para iterar sobre ele.


"""

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)
           
           
           ]

print(cidades)

# f = 9/5 * c + 32

# Lambda 

c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)
#print(c_para_f(('Berlim', 29)))

print(list(map(c_para_f, cidades)))

