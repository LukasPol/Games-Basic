def vence(jog,pc):
    print(f'O pc escolheu {pc}')
    if jog == pc:
        return 'Empate'
    elif jog == 'pedra' and pc == 'tesoura':
        return 'Jogador ganhou'
    elif jog == 'papel' and pc == 'pedra':
        return 'Jogador ganhou'
    elif jog == 'tesoura' and pc == 'papel':
        return 'Jogador ganhou'
    elif pc == 'pedra' and jog == 'tesoura':
        return 'PC ganhou'
    elif pc == 'papel' and jog == 'pedra':
        return 'PC ganhou'
    elif pc == 'tesoura' and jog == 'papel':
        return 'Pc ganhou'
