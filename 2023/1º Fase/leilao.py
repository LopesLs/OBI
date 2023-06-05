dictLances = {}
lances = int(input())

for index in range(lances):
  nome = input()
  valorLance = int(input())
  dictLances[nome] = valorLance

# verificar qual é o maior lance e printar o nome do vencedor junto do valor do lance

for nome, valorLance in dictLances.items():
  if valorLance == max(dictLances.values()):
    print(f'{nome}\n{valorLance}')
    break