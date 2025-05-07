#Faça um programa que determine e mostre os cinco primeiros múltiplos de um
#  número , considerando números maiores que 0.

contado: int = 0
indice: int = 1
multiplo: int = 0
numeroescolhido = int(input("Digite um número: "))
while contado < 5:
    multiplo = numeroescolhido * indice
    print(f"{numeroescolhido} x {indice} = {multiplo}")
    indice += 1
    contado += 1
print("Fim do programa")