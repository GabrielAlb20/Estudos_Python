"""
Decoradores (Decorators)

O que são decorators ?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açucar Sintático)

    \\--------------------------------------------------//
    \\               Function Decorator                 //
    \\--------------------------------------------------//


----------------------------------------------------------------
//   \\--------------------------------------------------//   //
//   \\                     Função                       //   //
//   \\--------------------------------------------------//   //
----------------------------------------------------------------





# Decorators como funções (Sintaxe não recomendada / Sem açucar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo(a) à Geek University')
    
    
    
# Testando 1

teste = seja_educado(saudacao)

teste()


    
# Testando 2

def raiva():
    print('EU TE ODEIO!')

raiva_educada = seja_educado(raiva)

raiva_educada()



# Decorators com Syntax Sugar (Açucar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo
        
        
        
@seja_educado_mesmo       
def apresentando():
    print('Meu nome é Pedro')
    
    
# Testando 

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')
    

dormir()

"""
"""
|-------------------------------------------------------------
|    Home     |   Serviços   |  Produtos  |  Administrativo  |
|-------------------------------------------------------------

http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/servicos
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin


# Não é código funcional (Que funcione) é apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')
        
def home(request):
    return 'Pode acessar home'
    

def servicoes(request):
    return 'Pode acessar serviços'
    
def produtos(request):
    return 'Pode acessar produtos'

@checa_login    
def admin(request)
    return 'Pode acessar produtos'
    
    
"""

# OBS: Não confunda Decorator com Decorator Function

