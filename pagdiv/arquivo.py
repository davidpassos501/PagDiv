def novoarq(arq):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{0}')
            a.close()
        except:
            print('Houve um ERRO na hora de escrever os dados!')


def existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler(arq):
    try:
        a = open(arq, 'rt')
        l = a.read().split(';')
        l.remove(l[-1])
        q = len(l)
        for c in range(0, q, 2):
            print(f'Pago R${int(l[c]):.2f} no dia {l[c-1]}')
    except:
        print('Erro ao ler arquivo!')


def leremp(arq):
    try:
        a = open(arq, 'rt')
        l = a.read().split(';')
        l.remove(l[-1])
        q = len(l)
        for c in range(0, q, 2):
            print(f'De R${int(l[c]):.2f} no dia {l[c-1]}')
    except:
        print('Erro ao ler arquivo!')


def pag(arq, valor, data):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{valor};{data};')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            v = int(valor)
            print(f'Novo pagamento de R${v:.2f}, no dia {data} feito com sucesso.')
            a.close()


def emp(arq, valor, data):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{valor};{data};')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            v = int(valor)
            print(f'Novo empréstimo de R${v:.2f}, no dia {data} feito com sucesso.')
            a.close()


def novopag(arq, arq2, valor):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{valor}')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            a.close()
            a = open(arq, 'rt')
            b = open(arq2, 'rt')
            teste1 = a.read().split('\n')
            teste2 = b.read().split('\n')
            num1 = int(teste1[0])
            num2 = int(teste2[0])
            novovalor = num2 - num1
            a.close()
            b.close()
            limpar(arq)
            limpar(arq2)
            c = open(arq2, 'at')
            c.write(str(novovalor))
            c.close()
            d = open(arq2, 'rt')
            teste3 = d.read().split('\n')
            t = int(teste3[0])
            print(f'A sua dívida restante é R${t:.2f}')
            d.close()


def novoemp(arq, arq2, valor):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{valor}')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            a.close()
            a = open(arq, 'rt')
            b = open(arq2, 'rt')
            teste1 = a.read().split('\n')
            teste2 = b.read().split('\n')
            num1 = int(teste1[0])
            num2 = int(teste2[0])
            novovalor = num2 + num1
            a.close()
            b.close()
            limpar(arq)
            limpar(arq2)
            c = open(arq2, 'at')
            c.write(str(novovalor))
            c.close()
            d = open(arq2, 'rt')
            teste3 = d.read().split('\n')
            t = int(teste3[0])
            print(f'A sua nova dívida é R${t:.2f}')
            d.close()


def limpar(arq):
    try:
        a = open(arq, 'w')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')


def teste(arq):
    a = open(arq, 'rt')
    t = a.read().split('\n')
    if int(t[0]) > 0:
        return True
    else:
        return False
