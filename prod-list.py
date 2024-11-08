lista = []

con = 0

while(con<5):
    n = int(input('insira um número inteiro'))

    con = con + 1

    lista.append(n)

    print('lista criada=',lista)

    print('soma das listas=',sum(lista))