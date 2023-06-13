lista = [[0, 1, 1, 1, 0], [0, 2, 0, 1, 1], [0, 0, 0, 0, 1], [3, 1, 1, 1, 1]]
passos = 0

if lista == None:
  exit()

def input_matriz(n, m, typer=str, question=''):
  resultado = []
  for x in range(n):
    entradas = input(question.format(x + 1)).split(' ')
    if (len(entradas) != m):
      print("ERRO!")
      return
    entradas = [typer(x) for x in entradas]
    resultado.append(entradas)
  return resultado
 
def verifica_sala(lista_atual, listaTotal):
  if lista_atual[lista_atual.index(3) - 1] < 0:
    pass
  else: 
    print(lista_atual[lista_atual.index(3) - 1])

  if lista_atual[lista_atual.index(3) + 1] > len(listaTotal):
    pass
  else:
    print(lista_atual[lista_atual.index(3) + 1])

for x in lista:
  if x.count(3) == 1:
    print('Está na lista', lista[lista.index(x)])
    verifica_sala(x, lista)
