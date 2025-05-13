'''
Teste de Velocidade com Expressões Geradoras



# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()

print(ge1) # Generator (<generator object nums at 0x000001EFEA53B510>)

print(next(ge1))
print(next(ge1))

# Generator Expression

ge2 = (num for num in range(1, 10))

print(ge2) # Generation Expression (<generator object <genexpr> at 0x000001EFEA4965C0>)

print(next(ge2))
print(next(ge2))

'''


# Realizando o teste de velocidade


import time

# Generator Expression
get_inicio = time.time()
soma_gen = sum(num for num in range(100000000)) 
gen_tempo = time.time() - get_inicio
print(f'Soma com Generator Expression: {soma_gen}')
print(f'Generator Expression levou {gen_tempo:.4f} segundos')

# List Comprehension
list_inicio = time.time()
soma_list = sum([num for num in range(100000000)]) 
list_tempo = time.time() - list_inicio
print(f'Soma com List Comprehension: {soma_list}')
print(f'List Comprehension levou {list_tempo:.4f} segundos')