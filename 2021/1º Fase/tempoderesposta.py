# Imcomplete code

users = {}

def tempo_gasto(time:int):
  return time

def mensagem_enviada(user:int):
  return user

def mensagem_recebida(user:int):
  return user

for evento in ['R 12', 'T 2', 'R 23', 'T 3', 'R 45', 'E 45', 'R 45', 'E 23', 'R 23', 'T 2', 'E 23', 'R 34', 'E 12', 'R 34']:
  
  if evento[0] == 'R':
    users[evento[2:]] = 1
  elif evento[0] == 'E':
    users[evento[2:]] += 1
  elif evento[0] == 'T':
    for user in users:
      users[user] += tempo_gasto(int(evento[2]))

for user in sorted(users):
  print(f'{user}: {users[user]}')