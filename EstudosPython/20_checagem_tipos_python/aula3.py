# Duck Typing

class CisneNegro:
    
    def __len__(self):
        return 42
    
livro = CisneNegro()

print(len(livro))

nome = 'Geek Universisty'
lista = [12, 34, 55, 49]
dicio = {"carlos": 12, "vanessa": 34, "joana": 49}

print(len(nome))
print(len(lista))
print(len(dicio))


idade = 42
peso = 81.4

# print(len(idade)) TypeError: object of type 'int' has no len()
