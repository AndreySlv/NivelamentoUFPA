par = []
impar = []
contador = 0

while contador != 10:
    valor = int(input("Informe um valor: "))
    contador += 1

    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print (f"números pares: {par}")
print (f"números impares: {impar}")