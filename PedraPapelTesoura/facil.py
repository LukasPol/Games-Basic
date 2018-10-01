import random
from objetos import obj

def facil():
    pc = random.choice(obj)
    print(',  '.join(obj), ' [ 0 p/ sair]')
    while True:
        jogador = input('Escolha um: ')
        if jogador == obj[0] or jogador == obj[1] or jogador == obj[2]:
            break
        elif jogador == '0':
            break
    return [jogador, pc]
