"""
- O rei decretou que o seguinte algotimo deve ser usado para cifrar os documentos:

- Cada consoante deve ser substituída por exatamente três letras, na seguinte ordem:
1. A própria consoante (vamos chamar de consoante original);
2. A vogal mais próxima da consoante original no alfabeto, com a regra adicional de que se a consoante original está à mesma distância de duas vogais, então a vogal mais próxima do início do alfabeto é usada. Por exemplo, se a consoante original é d, a vogal que deve ser usada é e, pois esta é a vogal mais próxima; se a consoante original é c, a vogal que deve ser utilizada é a, porque c está à mesma distância de a e e, e a é mais próxima do início do alfabeto.
3. A consoante que segue a consoante original, na ordem do início ao fim do alfabeto. Por exemplo, se a consoante original é d, a consoante a ser utilizada é f. No caso de a consoante original ser z, deve ser utilizada a própria letra z.

- As vogais não são modificadas.
Nesta tarefa, o alfabeto é
a b c d e f g h i j k l m n o p q r s t u v x z
e as vogais são
a e i o u
Por exemplo, a cifra da palavra "ter" é "tuveros" (tuv-e-ros) e a cifra da palavra "paz" é "poqazuz" (poq-a-zuz).

O rei da Nlogônia procura por alguém que saiba escrever um programa que produza a cifra de uma palavra dada. Você pode ajudá-lo?

"""

vogais = "a e i o u".split(' ')
alfabeto = "a b c d e f g h i j k l m n o p q r s t u v x z".split(' ')

def changeConsonant(charactere:str):
  charactereComplete = charactere
  
  if charactere in vogais:
    return charactere
  
  else:
    for index in range(3):
      consonanteOriginal = charactere
      DiffvogalProx = 25

      nextDiffVogalProx = (alfabeto.index(index) + 1) - (alfabeto.index(consonanteOriginal) + 1)

      if nextDiffVogalProx < 0:
        nextDiffVogalProx *= -1    

      if nextDiffVogalProx < DiffvogalProx:
        DiffvogalProx = nextDiffVogalProx
        print(index, 'é a mais próxima')


      print(index, ' -> ', alfabeto.index(index) + 1 , consonanteOriginal, ' -> ', (alfabeto.index(consonanteOriginal)) + 1, ' = ', DiffvogalProx)
    return

changeConsonant("t")