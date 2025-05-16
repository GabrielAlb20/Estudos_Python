"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:

a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.

"""

from datetime import date

from exercicio01 import Pessoa

class Agenda:
    
    def __init__(self):
        self.__contatos: list[Pessoa] = []
        
    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contatos
    
    def armazenar_contato(self, contato: Pessoa) -> None:
        self.contatos.append(contato)
    
    def remover_contato(self, contato: Pessoa) -> None:
        self.contatos.remove(contato)
    
    def buscar_contato(self, nome: str) -> None:
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O contato {nome} está na posição {indice}')
                
    def imprimir_agenda(self) -> None:
        for contato in self.contatos:
            contato.imprimir()
    
    def imprimir_contato(self, indice: int) -> None:
        self.contatos[indice].imprimir()
        
        
if __name__ == '__main__':
    
    contato1 = Pessoa(nome='Nayara Albuquerque', data_nascimento=date(year=2005, month=8, day=10), email='nayara@gmail.com')
    contato2 = Pessoa(nome='Gabriel Albuquerque', data_nascimento=date(year=2004, month=8, day=5), email='gabriel@gmail.com')
    contato3 = Pessoa(nome='Isabella Albuquerque', data_nascimento=date(year=2025, month=3, day=7), email='isabella@gmail.com')



agenda: Agenda = Agenda()

agenda.armazenar_contato(contato1)
agenda.armazenar_contato(contato2)
agenda.armazenar_contato(contato3)

agenda.imprimir_agenda()

agenda.buscar_contato('Isabella Albuquerque')

agenda.imprimir_contato(2)

agenda.remover_contato(contato3)

agenda.imprimir_agenda()


#contato1.imprimir()
#contato2.imprimir()
#contato3.imprimir()
