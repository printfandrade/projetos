while True :
    n1 = input("Digite um numero :")
    n2 = input("Digite outro número :")
    o = input("Digite um operador '+ - / * :'")
    if n1.isdigit() and n2.isdigit():
        if n1 != int(n1) or n2 != int(n2) :
            print('Voce digitou um numero invalido')
            if o == '+':
                print("Estou calculando")
                soma = int(n1) + int(n2)
                print(f"A soma dos valores é : {soma}")
            elif o == '-' :
                print("Estou calculando")
                sub = int(n1) - int(n2)     
                print (F"O valor da subtração é : {sub}") 
            elif o == '/' :
                print("Estou calculando")
                div = int(n1) / int(n2)
                print(f"O resultado da divisão entre {n1} e {n2} é : {int(div)}")
            elif o == '*' :
                print("Estou calculando")
                mult = int(n1) * int(n2)
                print(f'O valor da multiplicação entre {n1} e {n2} é : {mult}')
    
        if o != '' :
            print("Você digitou algum número invalido")
    sair = input('Voce quer sair? ').lower().startswith('s')
    if sair is True :
        break  