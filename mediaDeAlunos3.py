lista = []
nomes = []

print("=======Seja Bem-Vindo Professor(a)=======")
nAlunos = int(input("Quantos alunos a sua turma possuí?"))

for nota in range(nAlunos):
    aluno = input(f"Infome o nome do {nota+1}º aluno: ")
    nota = float(input(f"Informe a {nota+1}º nota: "))
    lista.append(nota)
    nomes.append(aluno)

med = sum(lista)/len(lista)

print("======LISTA DE ALUNOS E NOTAS======")
for i in range(nAlunos):
    print((f"nota do(a) aluno(a) {nomes[i]} : {lista[i]} "))

print(f"MÉDIA DOS ALUNOS: {med}")