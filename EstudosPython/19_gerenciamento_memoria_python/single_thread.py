# Single Thread
"""
    Em um programa single-threaded, todas as tarefas são executadas sequencialmente,
    uma após a outra, dentro de um único fluxo de execução (a thread principal).
    Imagine uma fila única onde cada pessoa (tarefa) precisa ser atendida completamente antes da próxima.
 """

import time
from threading import Thread

CONTADOR = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1
        
inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')

# Tempo em segundos: 0.8800497055053711