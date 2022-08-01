print("Informe o nome do aluno: ")
NomeAluno = input()

print("Informe a quantidade de notas: ")
QuantNota = int(input())
SomaNota = 0
   
for i in range(0, QuantNota):
    print(f"Informe nota N° {i+1}: ")

    Nota = input()
    while not Nota.isnumeric():
        print(f"Erro! Informe nota N° {i+1}: ")
        Nota = input()

    Nota = int(Nota)    
    SomaNota += Nota

print("o aluno: ", NomeAluno, " Ficou com a média: ", SomaNota/QuantNota)

print ("FIM DA EXECUÇÃO")