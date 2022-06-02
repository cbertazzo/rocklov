from math import factorial

qtdAlunos = int(input("Indique a quantidade de Alunos:"))

qtdElementos = int(input("Indique a quantidade de Elementos:"))

factorialAlunos = factorial(qtdAlunos)
factorialElementos = factorial(qtdElementos)
factorialDiferenca = factorial(qtdAlunos - qtdElementos)


gruposDiferentes = factorialAlunos/ (factorialElementos * factorialDiferenca)

print(f"Poderão ser formados {gruposDiferentes} grupos diferentes")




