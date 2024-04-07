#Função: O codigo só para quando receber um número positivo, enquanto receber número negativos é contabilizado as suas tentaivas!
contador = 1

while True:
    numero = int(input("Digite o número: "))
    if numero < 0:
        print("ELE É NEGATIVO")
        contador += 1
    else:
        print("ELE É POSITIVO")
        print(f"O número de tentavivas:{contador}")
        break