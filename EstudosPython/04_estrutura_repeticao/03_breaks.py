'''
 saindo de loops com break

 funciona da mesa forma que nas linguagems C ou java

 utilizamos o break para sair de loops de maneira projetada.
'''

#exemplo 1

'''for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
# O loop imprime os números de 1 a 5 e para quando chega a 6.
print('Sai do loop')'''

# exemplo 2 

while True:
    comando = input("Digite um 'sair' para sair: ")
    if comando == 'sair':
        break
    else:
        print('Você digitou:', comando)
print("você saiu do loop")
# O loop continua até que o usuário digite 'sair'.