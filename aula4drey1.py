from random import randint
vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    numAlet = randint(1,100)
    vetor1.append(numAlet)

    numAlet = randint(1,100)
    vetor2.append(numAlet)

for i2 in range(10):
    soma = vetor1[i2] + vetor2[i2]
    vetor3.append(soma)
print(vetor3)
