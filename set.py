nomes = set()
codigos = set()
completo = set()
while True:
    '''nome = input("nome: ")
    digito = input("codigo: ")
    nomes.add(nome)
    codigos.add(digito)
    completo.add(digito +'-'+ nome)'''
    nomes = {1,2,3,8,9}
    codigos = {3,5,6,7}
    diferenca = nomes - codigos 

    for i in diferenca:
        print(i)
    
    break
        