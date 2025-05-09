"""
Seek e Cursors 

seek() -> É utilizada para movimentar o cursor pelo arquivo.



arquivo = open('texto.txt')

print(arquivo.read())


# seek() -> A funçao seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um 
# Parametro que indica onde queremos colocar o cursor.
# Movimentando o cursor pelo arquivo com a função seek()  -> Procurar 
arquivo.seek(0) #

print(arquivo.read())

arquivo.seek(20)

print(arquivo.read())`


# readline() -> Funçao que ler  o arquivo linha a linha

print(arquivo.readline())

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))


"""

arquivo = open('texto.txt')

# readlines() 

print(arquivo.readlines())

print(len(arquivo.readlines()))
