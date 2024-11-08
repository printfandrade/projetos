import os

while True:

    cpf=input("Digite o cpf que deseja verificar: ")
    cpf_edit=cpf.replace('.','')
    os.system('cls')
    print(f'Aguarde! \nVerificando CPF: {cpf}')
    
    #cpf_digitos=cpf.split('.')
    #print(cpf_digitos)
    cpf_div=cpf_edit.split('-')
    verificadores, digitos = cpf_div
    cpf_usuario=f'{verificadores}-{digitos}'
    #print(digitos,verificadores)

    verificadores = '-'.join(verificadores)
    valores_str1 = verificadores.split('-')
    valores_str2 = verificadores.split('-')
    
    
    digitos_gerados=[]
    #print(valores_str)
    #print(valores_str2)

    c=int(10)
    
    for n in range(0, len(valores_str1)):
        
        valores_str1[n] = int(valores_str1[n])*c
        c-=1
    verificador_1= (sum(valores_str1)*10)%11
    digito_1 = verificador_1 if verificador_1 <= 9 else 0
    os.system('cls')

    print(f'O primeiro Digito Verificador é: {digito_1}')
    
    digitos_gerados.append(digito_1)
    valores_str2.append(digito_1)
    #print(valores_str2)

    c=int(11)
    
    for n in range(0, len(valores_str2)):
        
        valores_str2[n] = int(valores_str2[n])*c
        c-=1
    verificador_2= (sum(valores_str2)*10)%11
    digito_2 = verificador_2 if verificador_2 <= 9 else 0

    print(f'\nO segundo Digito Verificador é: {digito_2}')
    digitos_verificados=str(digito_1)+str(digito_2)

    verificadores_sistema=verificadores.replace('-','')
    cpf_verificado=f'{verificadores_sistema}-{digitos_verificados}'
    #print(cpf_verificado)

    if cpf_verificado==cpf_usuario:
        print('\nO CPF válido!')

        while True:

            opcoes=input("\n[V] - Verificar outro CPF | [S] - Sair: ").upper()
            
            if opcoes == 'V':
                break
            elif opcoes == 'S':
                quit()
            else:
                print("\nPor favor escolha uma opção válida!")
    
    else:
        os.system('cls')
        print('CPF inválido!\n')

        while True:

            opcoes=input("\n[D] - Digitar Novamente | [S] - Sair: ").upper()
            
            if opcoes == 'D':
                break
            elif opcoes == 'S':
                quit()
            else:
                print("\nPor favor escolha uma opção válida!")