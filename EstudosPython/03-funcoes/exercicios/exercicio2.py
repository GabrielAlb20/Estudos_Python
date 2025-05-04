''''
2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 20204”.
'''


def data_por_extenso(data:str) -> None:
    d = (data.split('/'))

    dia: int = int(d[0])
    mes: int = int(d[1])
    ano: int = int(d[2])

    if mes == 1:
        mes_str = 'Janeiro'
    elif mes == 2:
        mes_str = 'Fevereiro'
    elif mes == 3:
        mes_str = 'Março'
    elif mes == 4:
        mes_str = 'Abril'
    elif mes == 5:
        mes_str = 'Maio'
    elif mes == 6:
        mes_str = 'Junho'
    elif mes == 7:
        mes_str = 'Julho'
    elif mes == 8:
        mes_str = 'Agosto'
    elif mes == 9:
        mes_str = 'Setembro'
    elif mes == 10:
        mes_str = 'Outubro'
    elif mes == 11:
        mes_str = 'Novembro'
    elif mes == 12:
        mes_str = 'Dezembro'
    else:
        mes_str = 'Desconhecido'
    print(f'{dia} de {mes_str} de {ano}')
if __name__ == '__main__':
    data_por_extenso('01/02/2025')
