# Classe que representa uma televisão
class Televisao:
    
    def __init__(self):
        # Atributos privados com valores iniciais
        self.__status: bool = False  # TV começa desligada
        self.__volume: int = 10      # Volume inicial (de 0 a 100, por exemplo)
        self.__canal: int = 1        # Canal inicial (canal mínimo)

    # Getter e setter para o status (ligada ou desligada)
    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, status: bool) -> None:
        self.__status = status

    # Getter e setter para o volume
    @property
    def volume(self) -> int:
        return self.__volume

    @volume.setter
    def volume(self, volume: int) -> None:
        # Validação: impede volume abaixo de 0 ou acima de 100
        if 0 <= volume <= 100:
            self.__volume = volume

    # Getter e setter para o canal
    @property
    def canal(self) -> int:
        return self.__canal

    @canal.setter
    def canal(self, canal: int) -> None:
        # Validação: impede canais negativos ou nulos
        if canal >= 1:
            self.__canal = canal

    # Método para ligar ou desligar a TV
    def ligar_desligar(self) -> None:
        self.status = not self.status  # Inverte o estado (True <-> False)
        if self.status:
            print('📺 Status da TV: Ligada')
        else:
            print('📴 Status da TV: Desligada')

    # Método para aumentar o volume em 1 unidade
    def aumentar_volume(self) -> None:
        self.volume = self.volume + 1
        print(f'🔊 Volume da TV aumentado para: {self.volume}')

    # Método para diminuir o volume em 1 unidade
    def diminuir_volume(self) -> None:
        self.volume = self.volume - 1
        print(f'🔉 Volume da TV diminuído para: {self.volume}')

    # Método para aumentar o canal em 1 unidade
    def aumentar_canal(self) -> None:
        self.canal = self.canal + 1
        print(f'📺 Canal aumentado para: {self.canal}')

    # Método para diminuir o canal em 1 unidade
    def diminuir_canal(self) -> None:
        self.canal = self.canal - 1
        print(f'📺 Canal diminuído para: {self.canal}')

    # Método para mudar diretamente para um canal específico
    def mudar_canal(self, canal: int) -> None:
        self.canal = canal
        print(f'📺 Canal alterado diretamente para: {self.canal}')


# Classe que representa um controle remoto para a televisão
class ControleRemoto:
    
    def __init__(self, televisao: Televisao) -> None:
        # Recebe uma instância da classe Televisao para controlar
        self.__televisao: Televisao = televisao

    @property
    def televisao(self) -> Televisao:
        return self.__televisao

    # Todos os métodos abaixo são repassados para os métodos da televisão

    def ligar_desligar(self) -> None:
        self.televisao.ligar_desligar()

    def aumentar_volume(self) -> None:
        self.televisao.aumentar_volume()

    def diminuir_volume(self) -> None:
        self.televisao.diminuir_volume()

    def aumentar_canal(self) -> None:
        self.televisao.aumentar_canal()

    def diminuir_canal(self) -> None:
        self.televisao.diminuir_canal()

    def mudar_canal(self, canal: int) -> None:
        self.televisao.mudar_canal(canal)


# Execução principal do programa
if __name__ == '__main__':

    print("\n=== 🧪 Controle direto da TV ===")
    
    # Criando uma instância da TV
    tv = Televisao()
    
    # Testando os controles diretamente pela televisão
    tv.ligar_desligar()          # Liga a TV
    tv.aumentar_canal()          # Canal: 2
    tv.aumentar_canal()          # Canal: 3
    tv.aumentar_canal()          # Canal: 4
    tv.mudar_canal(42)           # Vai direto para o canal 42
    tv.aumentar_volume()         # Volume: 11
    tv.aumentar_volume()         # Volume: 12
    tv.aumentar_volume()         # Volume: 13
    tv.diminuir_canal()          # Canal: 41
    tv.diminuir_volume()         # Volume: 12
    tv.ligar_desligar()          # Desliga a TV

    print("\n=== 🎮 Controle via ControleRemoto ===")

    # Criando o controle remoto e associando à TV existente
    cr = ControleRemoto(tv)
    
    # Testando os mesmos comandos via controle remoto
    cr.ligar_desligar()          # Liga a TV
    cr.aumentar_canal()          # Canal: 42
    cr.aumentar_canal()          # Canal: 43
    cr.aumentar_canal()          # Canal: 44
    cr.mudar_canal(7)            # Vai direto para o canal 7
    cr.aumentar_volume()         # Volume: 13
    cr.aumentar_volume()         # Volume: 14
    cr.aumentar_volume()         # Volume: 15
    cr.diminuir_canal()          # Canal: 6
    cr.diminuir_volume()         # Volume: 14
    cr.ligar_desligar()          # Desliga a TV
