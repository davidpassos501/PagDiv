from arquivo import *
from data_atual import *
from leia import *
from menu import *

divida_total = 'divida_total.txt'
pagamento = 'pagamento.txt'
pagtemp = 'pagtemp.txt'
emprestimo = 'emprestimo.txt'
divtemp = 'divtemp.txt'
if not existe(divida_total):
    criar(divida_total)
    novoarq(divida_total)
if not existe(pagamento):
    criar(pagamento)
if not existe(pagtemp):
    criar(pagtemp)
if not existe(emprestimo):
    criar(emprestimo)
if not existe(divtemp):
    criar(divtemp)
data = data()
valor = 0
while True:
    cabecalho('\033[33mPagDiv\033[m')
    opc = menu(['Pagar', 'Novo Empréstimo', 'Pagamentos', 'Dívida Restante', 'Empréstimos', 'Sair'])
    if opc == 1:
        test = teste(divida_total)
        while True:
            if test:
                while True:
                    cabecalho('\033[32mPAGAR\033[m')
                    valor = leiaint('Quanto você quer pagar hoje? ')
                    pag(pagamento, valor, data)
                    novopag(pagtemp, divida_total, valor)
                    opc1 = menu(['Voltar', 'Sair'])
                    if opc1 == 1:
                        break
                    elif opc1 == 2:
                        exit()
            else:
                cabecalho('\n\033[34mParabéns você não tem dívidas pendentes!\033[m\n')
                opc0 = menu(['Voltar', 'Sair'])
                if opc0 == 1:
                    break
                elif opc0 == 2:
                    exit()


    elif opc == 2:
        while True:
            cabecalho('\033[32mNOVO EMPRÉSTIMO\033[m')
            empres = leiaint('Quanto você quer emprestado hoje? ')
            emp(emprestimo, empres, data)
            novoemp(divtemp, divida_total, empres)
            opc1 = menu(['Voltar', 'Sair'])
            if opc1 == 1:
                break
            elif opc1 == 2:
                exit()
    elif opc == 3:
        while True:
            cabecalho('\033[32mPAGAMENTOS\033[m')
            ler(pagamento)
            opc3 = menu(['Voltar', 'Sair'])
            if opc3 == 1:
                break
            elif opc3 == 2:
                exit()
    elif opc == 4:
        while True:
            cabecalho('\033[32mDÍVIDA RESTANTE\033[m')
            novopag(pagtemp, divida_total, valor)
            opc4 = menu(['Voltar', 'Sair'])
            if opc4 == 1:
                break
            elif opc4 == 2:
                exit()
    elif opc == 5:
        while True:
            cabecalho('\033[32mEMPRÉSTIMOS\033[m')
            leremp(emprestimo)
            opc5 = menu(['Voltar', 'Sair'])
            if opc5 == 1:
                break
            elif opc5 == 2:
                exit()
    elif opc == 6:
        break
