"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar e escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos  função write().
Esta função recebe uma string como parametro. caso contrário, teremos um TypeErro.



# Exemplo de escritas - modo 'w' - write (escrita)

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')
    

# O block with - Forma Pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)
    
# print(arquivo.read())

print(arquivo.closed)



# Forma tradicional de escrita em arquivo (Não Pythonica)

arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo.close()

with open('geek.txt','w') as arquivo:
    arquivo.write('Geek' * 1000)
"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informa uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
        else:
            break