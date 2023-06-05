valorDisponivel = int(input())
Acougue = int(input())
Farmacia = int(input())
Padaria = int(input())
contasPagas = 0

if valorDisponivel >= Acougue:
    valorDisponivel -= Acougue
    contasPagas += 1

if valorDisponivel >= Farmacia:
  valorDisponivel -= Farmacia
  contasPagas += 1

if valorDisponivel >= Padaria:
  valorDisponivel -= Padaria
  contasPagas += 1

print(contasPagas)