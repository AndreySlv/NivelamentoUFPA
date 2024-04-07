soma = 0
contador = 0

for n1 in range(0,20):
    n = int(input("Informe o número: "))
    if n > 0:
        soma = soma + n
    else:
        contador += 1
print (soma)
print (contador)

    