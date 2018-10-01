import os

pos = [[1, 2, 3],[ 4, 5, 6], [7, 8, 9]]
pos_remaining=[1,2,3,4,5,6,7,8,9]
pos_occupied=[]

cont=0
jogadas_P = 1

#=========== Funções ===================

# Função criação da placa..
def startBoard(): 
    #Escrevendo os nº
    for b in range (3):
        for c in range (3):
            print("{}".format(pos[b][c]),end="   " )
        print()


# Função Movimento 'X'..
def move_Player1(): 
    
    num = int(input('Jogador 1 [1-9]:\n'))
    if (num in pos_remaining):
        pos_occupied.append(num)
        pos_remaining.remove(num)
                
    else:    
        print('Posição já jogada, escolha outro némero...')
        move_Player1()
    

    #Para mudar o nº pelo 'X'     
    for d in range(len(pos)):
        for e in range(3):
            if num == pos[d][e]:
                pos[d][e] = 'X'

# Movimento 'O'
def move_Player2(): 
    
    num = int(input('Jogador 2 [1-9]:\n'))
    if (num in pos_remaining):
        pos_occupied.append(num)
        pos_remaining.remove(num)
                
    else:    
        print('Posição já jogada, escolha outro némero...')
        move_Player2()
    

    #Para mudar o nº pelo 'O'     
    for d in range(len(pos)):
        for e in range(3):
            if num == pos[d][e]:
                pos[d][e] = 'O'

def Verifica_X():
    win = True
    #Verificando linhas..
    if pos[0][0] == 'X' and pos[0][1] == 'X' and pos[0][2] == 'X':
        print('Player1 Ganhou')
        win = False
        #break
    elif pos[1][0] == 'X' and pos[1][1] == 'X' and pos[1][2] == 'X':
        print('Player1 Ganhou')
        win = False
        #break
    elif pos[2][0] == 'X' and pos[2][1] == 'X' and pos[2][2] == 'X':
        print('Player1 Ganhou')
        win = False
        #break
    
    #Verificando diagonais..
    elif pos[0][0] == 'X' and pos[1][1] == 'X' and pos[2][2] == 'X':
        print('Player1 Ganhou')
        win = False
        #break
    elif pos[0][2] == 'X' and pos[1][1] == 'X' and pos[2][0] == 'X':
        print('Player1 Ganhou')
        win = False
        #break

    #Verificando colunas..
    if pos[0][0] == 'X' and pos[1][0] == 'X' and pos[2][0] == 'X':
        print('Player1 Ganhou')
        win = False
        #break
    elif pos[0][1] == 'X' and pos[1][1] == 'X' and pos[2][1] == 'X':
        print('Player1 Ganhou')
        win = False
        #break
    elif pos[0][2] == 'X' and pos[1][2] == 'X' and pos[2][2] == 'X':
        print('Player1 Ganhou')
        win = False
        #break
    return win

def Verifica_O():
    win = True
    #Verificando linhas..
    if pos[0][0] == 'O' and pos[0][1] == 'O' and pos[0][2] == 'O':
        print('Player2 Ganhou')
        win = False
        #break
    elif pos[1][0] == 'O' and pos[1][1] == 'O' and pos[1][2] == 'O':
        print('Player2 Ganhou')
        win = False
        #break
    elif pos[2][0] == 'O' and pos[2][1] == 'O' and pos[2][2] == 'O':
        print('Player2 Ganhou')
        win = False
        #break
    
    #Verificando diagonais..
    elif pos[0][0] == 'O' and pos[1][1] == 'O' and pos[2][2] == 'O':
        print('Player2 Ganhou')
        win = False
        #break
    elif pos[0][2] == 'O' and pos[1][1] == 'O' and pos[2][0] == 'O':
        print('Player2 Ganhou')
        win = False
        #break

    #Verificando colunas..
    if pos[0][0] == 'O' and pos[1][0] == 'O' and pos[2][0] == 'O':
        print('Player2 Ganhou')
        win = False
        #break
    elif pos[0][1] == 'O' and pos[1][1] == 'O' and pos[2][1] == 'O':
        print('Player2 Ganhou')
        win = False
        #break
    elif pos[0][2] == 'O' and pos[1][2] == 'O' and pos[2][2] == 'O':
        print('Player2 Ganhou')
        win = False
    return win
#========================================
                
'''
===============================================
               Programa
===============================================

'''
def run():
    win = True
    cont = 0
    jogadas_P = 1
    startBoard()
    
    for a in range(5):
        if win == False:
            break
        
        
        #========Pedindo a posição de X e trocando..
        if jogadas_P <=5:
            move_Player1()
        else:
            break
                
        os.system("cls")
        startBoard()  
        win = Verifica_X()
        if win == False:
            break

        #=================Pedindo a posição Y e trocando...
        
        if jogadas_P <=4:
            move_Player2()
        else:
            print('Deu Velha')
            break
        
            
        os.system("cls")
        startBoard()
        win = Verifica_O()
        if win == False:
            break

        if a > 3:
            print('Deu Velha')
        jogadas_P+=1
       
    
