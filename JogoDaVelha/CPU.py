import os
import random

pos_remaining=[1,2,3,4,5,6,7,8,9]
pos_occupied=[]
pos = [[1, 2, 3],[ 4, 5, 6], [7, 8, 9]]
wins=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]            



#========= Funções ======================

# Função criação da placa..
def startBoard():
    for b in range (3):
        for c in range (3):
            print("{}".format(pos[b][c]),end="   " )
        print()


# Função Movimento 'X'..
def move_Player(): 
    
    num = int(input('pick a number from 1-9:\n'))
    if (num in pos_remaining):
        pos_occupied.append(num)
        pos_remaining.remove(num)
                
    else:    
        print('Position has been played, please pick again...')
        move_Player()
    
    #Para mudar o nº pelo 'X'     
    for d in range(len(pos)):
        for e in range(3):
            if num == pos[d][e]:
                pos[d][e] = 'X'
    

# Função Movimento 'CPU'..
def move_CPU():

    num = random.randint(1,9)
    if (num in pos_remaining):
        pos_occupied.append(num)
        pos_remaining.remove(num)
                
    else:
        move_CPU()
        
    #Para mudar o nº pelo 'O'     
    for d in range(len(pos)):
        for e in range(3):
            if num == pos[d][e]:
                pos[d][e] = 'O'

def Verifica_X():
    win = True
    #Verificando linhas..
    if pos[0][0] == 'X' and pos[0][1] == 'X' and pos[0][2] == 'X':
        print('Você Ganhou')
        win = False
        #break
    elif pos[1][0] == 'X' and pos[1][1] == 'X' and pos[1][2] == 'X':
        print('Você Ganhou')
        win = False
        #break
    elif pos[2][0] == 'X' and pos[2][1] == 'X' and pos[2][2] == 'X':
        print('Você Ganhou')
        win = False
        #break
    
    #Verificando diagonais..
    elif pos[0][0] == 'X' and pos[1][1] == 'X' and pos[2][2] == 'X':
        print('Você Ganhou')
        win = False
        #break
    elif pos[0][2] == 'X' and pos[1][1] == 'X' and pos[2][0] == 'X':
        print('Você Ganhou')
        win = False
        #break

    #Verificando colunas..
    if pos[0][0] == 'X' and pos[1][0] == 'X' and pos[2][0] == 'X':
        print('Você Ganhou')
        win = False
        #break
    elif pos[0][1] == 'X' and pos[1][1] == 'X' and pos[2][1] == 'X':
        print('Você Ganhou')
        win = False
        #break
    elif pos[0][2] == 'X' and pos[1][2] == 'X' and pos[2][2] == 'X':
        print('Você Ganhou')
        win = False
        #break
    return win

def Verifica_O():
    win = True
    #Verificando linhas..
    if pos[0][0] == 'O' and pos[0][1] == 'O' and pos[0][2] == 'O':
        print('A CPU ganhou')
        win = False
        #break
    elif pos[1][0] == 'O' and pos[1][1] == 'O' and pos[1][2] == 'O':
        print('A CPU ganhou')
        win = False
        #break
    elif pos[2][0] == 'O' and pos[2][1] == 'O' and pos[2][2] == 'O':
        print('A CPU ganhou')
        win = False
        #break
    
    #Verificando diagonais..
    elif pos[0][0] == 'O' and pos[1][1] == 'O' and pos[2][2] == 'O':
        print('A CPU ganhou')
        win = False
        #break
    elif pos[0][2] == 'O' and pos[1][1] == 'O' and pos[2][0] == 'O':
        print('A CPU ganhou')
        win = False
        #break

    #Verificando colunas..
    if pos[0][0] == 'O' and pos[1][0] == 'O' and pos[2][0] == 'O':
        print('A CPU ganhou')
        win = False
        #break
    elif pos[0][1] == 'O' and pos[1][1] == 'O' and pos[2][1] == 'O':
        print('A CPU ganhou')
        win = False
        #break
    elif pos[0][2] == 'O' and pos[1][2] == 'O' and pos[2][2] == 'O':
        print('A CPU ganhou')
        win = False
        #break
    return win    
#====================================
    
'''
==============================
    Programa Funcionar
==============================
'''
def run():
    win = True
    jogadas_P = 1
    jogadas_CPU = 1
    startBoard() # chamando a função


    for a in range(5):
        if win == False:
            break

        if jogadas_P <=5:
            move_Player()
        else:
            break
        
        if jogadas_CPU < 4:
            move_CPU()
        
        os.system("cls")
        startBoard()
        win = Verifica_X()
        if win == False:
            break
        win = Verifica_O()
        if win == False:
            break
        # =========== VELHA       
        if pos_remaining == []:
            print('Velha')
            break
        
        jogadas_CPU+=1
        jogadas_P+=1
        
#run()
