from random import randint
from time import sleep

'''Crie um jogo em que o computador jogue Jokenpô com você'''

esc = int(input('Aperte um número para escolher: 1 - Pedra, 2 - Papel ou 3 - Tesoura: '))

if esc == 1:
    esc = 'Pedra'
elif esc == 2:
    esc = 'Papel'
else:
    esc = 'Tesoura'



num = randint(1, 3)


if num == 1:
    num = 'Pedra'
elif num == 2:
    num = 'Papel'
else:
    num = 'Tesoura'

print('Jo...')
sleep(0.7)
print('ken...')
sleep(0.7)
print('pô!')
sleep(0.7)

#print(num)
#Aqui começa a condicional do PEDRA
if esc == 'Pedra' and num == 'Tesoura':
    print('Você escolheu {} e o computador {}, você VENCEU!'.format(esc.upper(), num.upper()))
elif esc == 'Pedra' and num == 'Papel':
    print('Você escolheu {} e o computador {}, você PERDEU!'.format(esc.upper(), num.upper()))
elif esc == 'Pedra' and num == 'Pedra':
    print('Você escolheu {} e o computador {}, EMPATE!'.format(esc.upper(), num.upper()))
#Aqui começa a condicional do PAPEL
elif esc == 'Papel' and num == 'Tesoura':
    print('Você escolheu {} e o computador {}, você PERDEU!'.format(esc.upper(), num.upper()))
elif esc == 'Papel' and num == 'Pedra':
    print('Você escolheu {} e o computador {}, você VENCEU!'.format(esc.upper(), num.upper()))
elif esc == 'Papel' and num == 'Papel':
    print('Você escolheu {} e o computador {}, EMPATE!'.format(esc.upper(), num.upper()))
# Aqui começa a condicional do TESOURA
elif esc == 'Tesoura' and num == 'Papel':
    print('Você escolheu {} e o computador {}, você VENCEU!'.format(esc.upper(), num.upper()))
elif esc == 'Tesoura' and num == 'Pedra':
    print('Você escolheu {} e o computador {}, você PERDEU!'.format(esc.upper(), num.upper()))
elif esc == 'Tesoura' and num == 'Tesoura':
    print('Você escolheu {} e o computador {}, EMPATE!'.format(esc.upper(), num.upper()))