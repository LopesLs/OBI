"""entrada = input().split(' ')"""
"""entrada = [int(x) for x in entrada]"""
lista = [['0', '1', '1', '1', '0'], ['0', '2', '0', '1', '1'], ['0', '0', '0', '0', '1'], ['3', '1', '1', '1', '1']]
passos = 0

"""for x in range(1, 5):
  lista.append(input().split(' '))"""

for x in lista:
  if x.count('2') == 1:
   # Verificando na Horizontal
   for y in range(len(x)):
    if x[x.index('2') - 1] == '1':
      passos += 1
    
    if x[x.index('2') + 1] == '1':
      passos += 1
    
    break
  
  # Verificando na Vertical
   print(lista[lista.index(x) - 1][x.index('2')] == '1') 

for x in lista:
  print(x, lista.index(x))

print(passos)
