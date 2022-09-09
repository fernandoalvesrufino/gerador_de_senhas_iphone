# Gerador de senhas do iPhone

import random, string

for i in range(3):
  for _ in range(6):
    print(f'{random.choice(string.digits + string.ascii_letters)}', end='')
  if i != 2:
    print('-', end='')
  else:
    print('')
