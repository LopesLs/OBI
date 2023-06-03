saloesTuneis = input().split()
saloesTuneis = [int(x) for x in saloesTuneis]
conexoes = {}
sugestaoPossiveis = 0

for conexao in range(saloesTuneis[0]):
  conexoes[conexao+1] = []

for saloes in range(saloesTuneis[1]):
  conexao = input().split()
  conexao = [int(x) for x in conexao]
  conexoes[conexao[0]].append(conexao[1])
  conexoes[conexao[1]].append(conexao[0])

passeios = int(input())

for x in range(passeios):
  isAndavel = True
  saloes = input().split()
  saloes = [int(x) for x in saloes]

  for i in range(len(saloes)):
    if i == 0:
      continue 
    if i == len(saloes) - 1:
      break
    if saloes[i+1] not in conexoes[saloes[i]]:
      isAndavel = False
  
  if isAndavel:
    sugestaoPossiveis += 1

print(sugestaoPossiveis)