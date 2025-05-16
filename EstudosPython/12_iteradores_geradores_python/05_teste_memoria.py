''''
Teste de Memória com Generators

# Sequencia de Fibonacci
1, 1, 2, 3, 5, 8, 13...

'''

# Função usando listas 497MB
import sys

# Aumente o limite para um valor maior, por exemplo, 1000000 (um pouco mais alto, já que a lista pode ter muitos números grandes)
sys.set_int_max_str_digits(1000000)

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste
#for n in fib_lista(100000):
   # print(n)


# Função usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste 2 Geradores 10MB

for n in fib_gen(100000):
    print(n)