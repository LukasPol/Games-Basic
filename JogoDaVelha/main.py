import CPU
import doisPlayers

while True:
    print('''
 = = = = = = = = = = = = = = = 
|                             |
|             Seja            |
|          Bem-vindo!!        |
|                             |
| --------------------------- |
|                             |
|    TIPOS DE JOGOS:          |
|                             |
| 1 - 2 Players               |
| 2 - VS CPU                  |
| 3 - Sair                    |
 = = = = = = = = = = = = = = =
''')
    jogo = int(input('Escolha o estilo de jogo '))
    if jogo == 1:
        doisPlayers.run()
    elif jogo == 2:
        CPU.run()
    elif jogo == 3:
        break
