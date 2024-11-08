import os

lista_compras = []

titulo=input("Qual Titulo da sua lista? ").upper()

def ler_lista():
    print(f"\n{titulo}\n")
    for indice, item in enumerate(lista_compras, start=1):
        print(indice, item)

def menu():
    print('\n[I] - Inserir Item \n[M] - Modificar Item \n[D] - Deletar Item \n[L] - Listar \n[S] - Sair'
               .upper())
    
def erro():
    try:
        funcao()

    except ValueError:
        print('Digite um valor válido!')

    except IndexError:
        print('O indice selecionado não existe na lista!')

    except Exception:
        print('Erro desconhecido!')    
    
while True :

    menu()

    opcoes =  input("\nSelecione uma opção: ").upper()

    if opcoes == "I":
        os.system('cls')
        novo_item=input("Adicione o novo item: ")
        lista_compras.append(novo_item)

    elif opcoes == "M":
        os.system('cls')
        if len(lista_compras) == 0:

            print('Sua lista ainda está vázia!')

        else:
            os.system('cls')
            
            ler_lista()

            indice=input("Digite o idice do item que deseja modificar: ")

            indice_int=int(indice) - 1
                            
            def funcao():

                lista_compras[indice_int]=input("Adicione o novo item: ")

                ler_lista()

            erro()

    elif opcoes == "D":

        if len(lista_compras) == 0:

            print('Sua lista ainda está vázia!')

        else:
            os.system('cls')
            indice=input("Digite o idice do item que deseja deletar: ")

            def funcao():
                indice = int(indice)
                del lista_compras[indice]

                ler_lista()

            erro()

    elif opcoes == "L":
        os.system('cls')
        if len(lista_compras) == 0:

            print('Sua lista ainda está vázia!')
        else:
            os.system('cls')
            
            ler_lista()

        while True:

            opcoes=input("[R] - Retornar ao menu Inicial | [S] - Sair: ").upper()
            
            if opcoes == 'R':
                break
            elif opcoes == 'S':
                quit()
            else:
                print("\nPor favor escolha uma opção válida!")

    elif opcoes == "S":
         os.system('cls')
         break

    else:
        os.system('cls')
        print("\nPor favor escolha uma opção válida!")