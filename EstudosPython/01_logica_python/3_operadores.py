# Operadores Aritméticos
print("--- Operadores Aritméticos ---")
a = 10
b = 3
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")
print()

# Operadores de Atribuição
print("--- Operadores de Atribuição ---")
x = 5
print(f"x (inicial) = {x}")
x += 2
print(f"x += 2 (x = x + 2) = {x}")
x -= 1
print(f"x -= 1 (x = x - 1) = {x}")
x *= 3
print(f"x *= 3 (x = x * 3) = {x}")
x /= 2
print(f"x /= 2 (x = x / 2) = {x}")
x //= 2
print(f"x //= 2 (x = x // 2) = {x}")
x %= 2
print(f"x %= 2 (x = x % 2) = {x}")
x **= 3
print(f"x **= 3 (x = x ** 3) = {x}")
print()

# Operadores de Comparação
print("--- Operadores de Comparação ---")
p = 7
q = 10
print(f"p == q: {p == q}")
print(f"p != q: {p != q}")
print(f"p > q: {p > q}")
print(f"p < q: {p < q}")
print(f"p >= q: {p >= q}")
print(f"p <= q: {p <= q}")
print()

# Operadores Lógicos
print("--- Operadores Lógicos ---")
verdadeiro = True
falso = False
print(f"verdadeiro and falso: {verdadeiro and falso}")
print(f"verdadeiro or falso: {verdadeiro or falso}")
print(f"not verdadeiro: {not verdadeiro}")
print()

# Operadores Bitwise
print("--- Operadores Bitwise ---")
num1 = 5  # Em binário: 0101
num2 = 3  # Em binário: 0011
print(f"num1 & num2 (AND): {num1 & num2} (binário: {bin(num1 & num2)})")
print(f"num1 | num2 (OR): {num1 | num2} (binário: {bin(num1 | num2)})")
print(f"num1 ^ num2 (XOR): {num1 ^ num2} (binário: {bin(num1 ^ num2)})")
print(f"~num1 (NOT): {~num1} (binário: {bin(~num1)})") # Observe o resultado para números negativos
print(f"num1 << 1 (Left Shift): {num1 << 1} (binário: {bin(num1 << 1)})")
print(f"num1 >> 1 (Right Shift): {num1 >> 1} (binário: {bin(num1 >> 1)})")
print()

# Operadores de Identidade
print("--- Operadores de Identidade ---")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print(f"lista1 is lista2: {lista1 is lista2}") # False, são objetos diferentes na memória
print(f"lista1 is lista3: {lista1 is lista3}") # True, ambas referem-se ao mesmo objeto
print(f"lista1 is not lista2: {lista1 is not lista2}")
print()

# Operadores de Associação
print("--- Operadores de Associação ---")
frutas = ["maçã", "banana", "laranja"]
print(f"'banana' in frutas: {'banana' in frutas}")
print(f"'uva' in frutas: {'uva' in frutas}")
print(f"'morango' not in frutas: {'morango' not in frutas}")