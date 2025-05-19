"""
A principal razão para usar multiprocessing é para tarefas que são intensivas em CPU. Como mencionado anteriormente,
devido ao GIL, threads em Python não conseguem executar código Python bytecode simultaneamente em múltiplos núcleos.
Processos, por outro lado, são entidades separadas pelo sistema operacional e podem ser distribuídos entre os núcleos da CPU,
permitindo uma aceleração significativa para cálculos complexos.
    
"""
import time
from multiprocessing import Pool

CONTADOR = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    r2 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f'Tempo em segundos: {fim - inicio}')
    
 # Tempo em segundos: 0.4931497573852539 - Mais performance