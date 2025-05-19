# Execução em Múltiplas Threads

"""
Em um programa multi-threaded, diferentes partes do programa podem ser executadas concorrentemente. Imagine várias filas sendo
atendidas simultaneamente por diferentes atendentes (threads). No entanto, a forma como o Python implementa multi-threading
 tem algumas nuances importantes devido ao Global Interpreter Lock (GIL).
"""

import time
from threading import Thread

CONTADOR = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1
        
t1 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'Otempo em segundos: {fim - inicio}')

# Otempo em segundos: 0.8645963668823242