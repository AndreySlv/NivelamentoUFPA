peso = float(input("Informe seu peso:"))
altura = float(input("Informe sua altura:"))

imc = peso//(altura**2)

if imc < 18.5:
    print(f" {imc} = Abaixo do peso")
elif imc > 18.5 and imc < 24.9:
    print(f'{imc} = Peso normal')
elif imc > 25.0 and imc < 29.9:
    print(f'{imc} = Sobrepeso')
else:
    print(f'{imc} = Você está Obeso')
    