print("==========CONVERSOR DE MEDIDAS M E CM==========")
conv = int(input("Qual conversão deseja fazer, digite um número positivo para (de metro para centímetros) ou um número negativo para (de centímetros para metros)?"))
numero1 = int(input("Digite o número que deseja converter: "))
if conv > 0:
    res = numero1 * 100
    print(f"Resultado = {res}")
else:
    res = numero1 / 100
    print(f"Resultado = {res}")

int(input("informe um número inteiro : "))
float(input("informe um número decimal : "))
str(input("informe uma palavra : ")) or (input("informe uam palavra: "))
bool(input("informe um número  : "))