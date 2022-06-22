def computador_escolhe_jogada(n, m):
    computadorRemove = 1

    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove

        else:
            computadorRemove += 1

    return computadorRemove


def usuario_escolhe_jogada(n, m):
    jogadaValida = False

    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()

        else:
            jogadaValida = True

    return jogadorRemove


def campeonato():
    nRodada = 1
    while nRodada <= 3:
        print()
        print('**** Rodada', nRodada, '****')
        print()
        partida()
        nRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')


def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    vezDoPC = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', computadorRemove, 'peças')

            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogadorRemove, 'peças')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')

tipoDePartida = int(input('2 - para jogar um campeonato '))

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()