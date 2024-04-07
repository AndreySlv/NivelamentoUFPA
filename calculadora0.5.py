ope = 0
while True:
    print("Para realizar uma: soma 1, subtração 2, divisão inteira 3, divisão decimal 4, exponenciação 5, multiplicação 6 ou para sair digite 7 ")
    ope = int(input("Qual operação deseja realizar? "))
    if ope < 0:
        print("essa operação não esta registrada")
    elif ope >= 8:
        print("essa operação não esta registrada")
    n1 = int(input("Adicione o primeiro número: "))
    n2 = int(input("Adicione o segundo número: "))
    if ope == 1:
        res = n1 + n2
        ope = "+"
    elif ope == 2:
        res = n1 - n2
        ope = "-"
    elif ope == 3:
        res = n1 // n2
        ope = "/"
    elif ope == 4:
        res = n1 / n2
        ope = "/"
    elif ope == 5:
        res = n1 ** n2
        ope = "^"
    elif ope == 6:
        res = n1 * n2
        ope = "x"

    print(f" {n1} {ope} {n2} = {res}")
    i = int(input("Para continuar digite 1, para sair digite 0: "))
    if i == 1:
        print("====================================================================================")
    else:
        print("Obrigado por me utilizar, Volte sempre!")
        break
    