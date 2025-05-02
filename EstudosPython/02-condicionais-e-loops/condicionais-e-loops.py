"""Estruturas de Decisão (Condicionais)"""


# Estrutura condicional simples
idade = 20

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Estrutura condicional com elif
nota = 7

if nota >= 9:
    print("Aprovado com distinção!")
elif nota >= 6:
    print("Aprovado.")
else:
    print("Reprovado.")



# Condicional Aninhada


# Condicional dentro de outra condicional
idade = 16
tem_cnh = False

if idade >= 18:
    if tem_cnh:
        print("Você pode dirigir!")
    else:
        print("Você é maior de idade, mas não tem CNH.")
else:
    print("Você é menor de idade e não pode dirigir.")



# Laços de Repetição(Loops)

# Loop que imprime números de 1 a 5
for i in range(1, 6):
    print(i)

# Loop para percorrer uma lista
nomes = ["Ana", "Carlos", "Pedro", "Maria"]

for nome in nomes:
    print(f"Olá, {nome}!")




# Loop (While)



# Loop que imprime números de 1 a 5 usando while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Incrementa o contador

# Exemplo de loop com condição de saída
numero = 0
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        print("Saindo do loop...")
        break
    print(f"Você digitou: {numero}")





# Controle de Fluxo (Break e Continue)

# Usando break para sair do loop antecipadamente
for i in range(10):
    if i == 5:
        print("Número 5 encontrado, saindo do loop.")
        break
    print(i)

# Usando continue para pular a iteração atual
for i in range(10):
    if i % 2 == 0:  # Se for número par, pula
        continue
    print(i)
