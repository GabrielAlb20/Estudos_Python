"""
 POO - Atributos 
   
Atributos -> Representam as características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos Dinâmicos;

# Atributo de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.


# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampda(){
    private int voltagem;
    public String cor;
    protected Boolean ligada = false;
    
    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
    public int getVoltagem(){
        return this.voltagem
    }
}

Em Python por convenção, ficou estabelecido que, todo o atributo de uma classe é púlblico
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling.






# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagm Python não
# vai impedir que façamos acesso aos aributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)

#print(user.__senha) # AttributeError

print(user._Acesso__senha) # Temos acesso. Mas não deveríamos fazer este acesso. (Name Mangling)

user.mostra_email()
user.mostra_senha()



# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias 
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()



p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor) # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor) # Acesso possível, mas incorreto de um atributo de classe

# Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;



"""
# Classes com Atributo de Instância Púlblico
class Lampada:
    """
    Esta classe representa uma lâmpada com suas características e funcionalidades básicas.
    """
    # Método construtor (__init__):
    # Este é um método especial em Python que é chamado automaticamente
    # quando um novo objeto (instância) da classe Lampada é criado.
    # Ele é usado para inicializar os atributos do objeto.
    def __init__(self, voltagem, cor):
        # 'self' é uma convenção em Python e representa a instância da classe
        # que está sendo criada. Através de 'self', podemos acessar e definir
        # os atributos do objeto.

        # self.voltagem = voltagem:
        # Aqui, estamos criando um atributo chamado 'voltagem' para o objeto Lampada.
        # O valor que este atributo irá receber é o valor passado como argumento
        # para o parâmetro 'voltagem' no momento da criação do objeto.
        self.voltagem = voltagem  # Atributo que armazena a voltagem da lâmpada.

        # self.cor = cor:
        # Similarmente, criamos um atributo chamado 'cor' para armazenar a cor da lâmpada.
        # O valor deste atributo será o valor passado para o parâmetro 'cor'.
        self.cor = cor        # Atributo que armazena a cor da lâmpada.

        # self.ligada = False:
        # Criamos outro atributo chamado 'ligada' para indicar se a lâmpada está ligada ou não.
        # Inicializamos este atributo com o valor False, o que significa que, por padrão,
        # uma nova lâmpada criada estará desligada.
        self.ligada = False    # Atributo booleano que indica se a lâmpada está ligada (True) ou desligada (False).
        
        
class ContaCorrente:
    
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
            
#class Produto:
    
  #  def __init__(self, nome, descricao, valor):
      #  self.nome = nome
     #   self.descricao = descricao
     #   self.valor = valor
        
class Usuario:
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
class Teste:
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.idade = email
        self.senha = senha
        

# Atributos Púlblicos e Atributos Privados 

class Acesso:
    
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)
        
    def mostra_email(self):
        print(self.email)
        
# Atributos de Classe

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as istâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios 
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo.

# Refatorar a classe Produto

class Produto:
    
    imposto = 1.05 # 0.05% de imposto
    contador = 0 # Atributo de classe
    
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id # Atributo de classe
        
        
# Atributos Dinâmicos  -> Um atributos de instâncias que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg' # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

# print(f'Produto: {p1.nome}, Descrição {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)