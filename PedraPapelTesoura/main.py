from facil import facil
from medio import medio
from vencedor import vence
import objetos
import os


while True:
    print('''
 = = = = = = = = = = = = = = = 
|                             |
|             Seja            |
|          Bem-vindo!!        |
|                             |
| --------------------------- |
|                             |
|       TIPOS DE JOGOS:       |
|                             |
| 1 - Fácil                   |
| 2 - Médio                   |
| 3 - Sair                    |
 = = = = = = = = = = = = = = =
''')
    jogo = int(input('Escolhe o nivel do jogo: '))
    if jogo == 1 :
        x = facil()
        if x[0] == '0':
            break
        else:
            print(vence(x[0],x[1]))  
    elif jogo ==2:
        x = medio()
        if x[0] == '0':
            break
        else:
            print(vence(x[0], x[1]))
    elif jogo == 3:
        break
    else:
        os.system('cls')
    print()
