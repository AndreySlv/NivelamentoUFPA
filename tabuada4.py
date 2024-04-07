numero = int(input("Informe o número da tabuada que deseja visualizar: "))
numero2 = 0

print(f"tabuada do {numero}")
while numero2<10:
    numero2 += 1
    print(f"{numero}x{numero2}={numero*numero2}")