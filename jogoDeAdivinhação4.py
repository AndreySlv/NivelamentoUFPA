from random import randint
numeroAleatorio = randint(1,20)

print ("___JOGO DA ADVINHAÇÃO___")

numero = 0
chute = 0

print(numeroAleatorio)
while numero != numeroAleatorio:
    numero = int(input("Digite o número que está pensando: "))
    chute += 1
    
    if chute == 4:
        print("cabô o número de tentativas")
        break
    if numero < numeroAleatorio:
        print("O número informado está abaixo do desejado")  
    elif numero > numeroAleatorio:
        print("O número informado está acima do desejado")
    else:
        print("Parabéns você acertou o número!")
        print(f"Número de tentaivas: {chute}")
