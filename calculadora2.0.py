operacao = 0

def calculadora(a, operacao , c):
    if operacao == 1:
        resultado = a * c
        operacao = "x"
    elif operacao == 2:
        resultado = a + c
        operacao = "+"
    elif operacao == 3:
        resultado = a - c
        operacao = "-"
    elif operacao == 4:
        resultado = a // c
        operacao = "÷"
    elif operacao == 5:
        resultado = a / c
        operacao = "÷"
    elif operacao == 6:
        resultado = a ** c
    return resultado

def calcularFatorial(a):
    if a == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, a +1):
            resultado *= i
        return resultado

while True:
    texto = """
    ============CALCULADORA============
    multiplicação = 1
    soma = 2
    subtração = 3
    divisão inteira = 4
    divisão decimal = 5
    exponenciação = 6
    fatorial = 7
    sair = 0
    """
    print(texto)

    operacao = int(input("Escolha o tipo da operação: "))

    if operacao == 0:
        print("Obrigad(o/a/e) por me utilizar, volte sempre!")
        break
    elif operacao < 0 or operacao >= 8:
        print("Essa operação não estar na tabela! \n tente novamente por favor :)")
    elif operacao != 7:
        numb1 = int(input("Escolha o primeiro número: "))
        numb2 = int(input("Escolha o segundo número : "))
        calculando = calculadora(numb1,operacao,numb2)
        print(f"{numb1} {operacao} {numb2}")

        print(f"O resultado é {calculando}")
    elif operacao == 7:
        numb1 = int(input("Escolha o número: "))
        calculando = calcularFatorial(numb1)
        print
        print(f"O fatorial de {numb1} é {calculando}")
