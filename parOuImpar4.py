pares = []
impares = []

for contador in range(10):
    valor = int(input("Informe o valor: "))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(pares)
print(impares)