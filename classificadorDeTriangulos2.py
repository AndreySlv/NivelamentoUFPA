print("=======Classificador de Triângulo=======")
print("Digite os valores de cada lado do triângulo para que seja classificado")
a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input('Digite o terceito valor:'))

if a<b+c and b<a+b and c<b+a:
    if a!=b!=c:
        print('é um triângulo escaleno')
    elif a==b==c:
        print("é um triângulo equilátero")
    else:
        print('é um triângulo isóceles')
else:
    print("não é um triângulo")