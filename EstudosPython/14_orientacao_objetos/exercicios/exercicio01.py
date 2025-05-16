from datetime import date


class Pessoa:
    """
    Esta classe representa uma pessoa com nome, data de nascimento e email.
    """

    def __init__(self, nome: str, data_nascimento: date, email: str) -> None:
        """
        Inicializa um objeto Pessoa.

        Args:
            nome (str): O nome da pessoa.
            data_nascimento (date): A data de nascimento da pessoa.
            email (str): O email da pessoa.
        """
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__email = email

    @property
    def nome(self) -> str:
        """Obtém o nome da pessoa."""
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """Define o nome da pessoa."""
        self.__nome = nome

    @property
    def data_nascimento(self) -> date:
        """Obtém a data de nascimento da pessoa."""
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        """Define a data de nascimento da pessoa."""
        self.__data_nascimento = data_nascimento

    @property
    def email(self) -> str:
        """Obtém o email da pessoa."""
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        """Define o email da pessoa."""
        self.__email = email

    def imprimir(self) -> None:
        """Imprime os dados da pessoa formatados."""
        print(f'Nome: {self.__nome}')
        print(f'E-mail: {self.__email}')
        print(f'Data Nascimento: {self.__data_nascimento.strftime("%d/%m/%Y")}')


if __name__ == '__main__':
    # Criando um objeto Pessoa
    p = Pessoa(nome='Felicity Jones', data_nascimento=date(year=1987, month=7, day=22), email='felicity@gmail.com')

    # Imprimindo os dados da pessoa
    p.imprimir()
