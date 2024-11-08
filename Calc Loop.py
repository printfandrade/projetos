ni=input("Determine o inicio do Loop: ")

nf=input("Determine o final do Loop: ")

passo=input("Determine o passo do Loop: ")

operador=input("Determine a operação agregada ao Loop (+-*/): ")

valor=input("Determine o valor agregado a operação: ")

ni=float(ni)
nf = float(nf)
passo = float(passo)
valor = float(valor)
loop=ni-passo
operacao = loop

while loop <= nf-passo:

    loop += passo

    if operador == "+":
        operacao = loop+valor
        print( f"{loop} {loop} + {valor} = {operacao}")
    
    if operador == "-":
        operacao = loop-valor
        print( f"{loop} {loop} - {valor} = {operacao}")
    
    if operador == "*":
        operacao = loop*valor
        print( f"{loop} {loop} * {valor} = {operacao}")

    if operador == "/":
        operacao = loop/valor
        print( f"{loop} {loop} / {valor} = {operacao}")