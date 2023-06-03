quantidade = int(input())
numeros = []

for index in range(quantidade):
    numero = int(input())
    
    if (numero == 0):
      numeros.pop()
    else:
      numeros.append(numero)

print(sum(numeros))