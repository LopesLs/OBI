entradas = input().split(' ')
numeroTipos = int(entradas[0])
numeroTamanhos = int(entradas[1])
matriz = []
totalVendas = 0

for i in range(numeroTipos):
  for j in range(numeroTamanhos):
    valor = input().split(' ')
    matriz.append(valor)
    break

pedidos = int(input())

for i in range(pedidos):
  valor = input().split(' ')
  x, y = int(valor[0]), int(valor[1])
  
  if int(matriz[x-1][y-1]) > 0:
    totalVendas += 1
    matriz[x-1][y-1] = int(matriz[x-1][y-1]) - 1
  else:
    continue

print(totalVendas)