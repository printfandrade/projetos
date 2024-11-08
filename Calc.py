n1 = input("Digite o primeiro termo da equação: ")
n2 = input("Digite o segundo termo da equação: ")
eq = input("Escolha a função '+, -, *, /': ")

while 'true' :
    print (f"{n1}")
    print (f"{n2}")
    n3 = 0
    n4 = 0 
    if not n1.isdigit() or not n2.isdigit():
    
        print ("Um dos termos não é um número inteiro!")
    else : 
        if  eq == '+' :
            eq1 = n3 + n4
            print (f"Seu resultado é {eq1}!")

        elif eq == '-' :
            eq2 = int(n1) - int(n2)
            print (f"Seu resultado é {eq2}!")
            
        elif eq == '*' :
            eq3 = int(n1) * int(n2)
            print (f"Seu resultado é {eq3}!")

        elif eq == '/' :
            eq4 = int(n1) / int(n2)
            print (f"Seu resultado é {int(eq4)}!")
    
    break