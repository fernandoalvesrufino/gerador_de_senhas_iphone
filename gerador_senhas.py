# Gerador de senhas do iPhone

import random, string                   # Importando bibliotecas random utilizada para gerar números aleatórios
                                        # Importando bibliotecas string
for i in range(3):                      # Para cada elemento i num range de 3 elementos
  for _ in range(6):                    # Para cada elemento num range de 6 elementos
    print(f'{random.choice(string.digits + string.ascii_letters)}', end='')
    # imprime um caracter aleatório entre letras e numeros
  if i != 2:                            # se o elemento i for diferente de 2
    print('-', end='')                  # imprimir '-' após os seis caracteres aleatórios
  else:                                 # senão se for igual a 2
    print('')                           # não imprimir nada (para que não tenha um traço no final da senha)
