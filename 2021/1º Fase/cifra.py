vogais = "a e i o u".split(' ')
consoantes = "b c d f g h j k l m n p q r s t v x z".split(' ')
alfabeto = "a b c d e f g h i j k l m n o p q r s t u v x z".split(' ')
output = ""

# Função que retorna a próxima consoante
def nextConsonant(charactere:str):
  if charactere == 'z':
    return 'z'
  else:
    index = alfabeto.index(charactere)
    nextConsonants = alfabeto[index + 1:]
    
    for letra in nextConsonants:
      if letra in consoantes:
        return letra

# Função que retorna a vogal mais próxima
def proxVogal(charactere:str):
  DiffvogalProx = 25
  vogalProx = ''

  for letra in alfabeto:
    nextDiffVogalProx = (alfabeto.index(letra) + 1) - (alfabeto.index(charactere) + 1)

    if nextDiffVogalProx < 0:
      nextDiffVogalProx *= -1    

    if nextDiffVogalProx < DiffvogalProx:
      if letra in vogais:
        DiffvogalProx = nextDiffVogalProx
        vogalProx = letra

  return vogalProx

for letra in input():
  if letra in vogais:
    output += letra
  else:
    for i in range(3):
      if i == 0:
        output += letra
      elif i == 1:
        output += proxVogal(letra)
      elif i == 2:
        output += nextConsonant(letra)

print(output)