import time
nome = input('Qual é o seu nome? ')
contador = 11
while contador>1:
    contador -=1
    time.sleep(0.5)
    print(contador)
print(f"Feliz Ano Novo {nome}!")