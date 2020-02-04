from datetime import date


def data():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    lista = [f'{dia}/{mes}/{ano}']
    for c in lista:
        return c
