import random
from objetos import obj

def medio():
    print(',  '.join(obj), ' [ 0 p/ sair]')
    while True:
        jogador = input('Escolha um: ')
        if jogador == obj[0] or jogador == obj[1] or jogador == obj[2]:
            while True:
                pc = random.choice(obj)
                if pc != jogador:
                    break
            return [jogador, pc]
            break
        elif jogador == '0':
            return [jogador]
            break
    
