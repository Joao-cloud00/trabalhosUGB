import random
from random import choice


pc_vitorias = 0
jogador_vitorias = 0
empates = 0


def jogador():
    esc_jogador = input('Escolha, par ou ímpar: ')

    if esc_jogador in ['ímpar','ÍMPAR','Ímpar','ÍMpar','ÍMPar','ÍMPAr','ÍMpAr','ÍMpAR','ÍMpaR']:
        esc_jogador == 'ímpar'
        
    elif esc_jogador in ['par','Par','PAR','PaR','PAr']:
        esc_jogador == 'par'

    else:
        print('Opção inválida. Tente novamente')
        jogador()
    return esc_jogador

def computador():

    esc_computador = choice(('par', 'ímpar'))
    return esc_computador

def jogada_computador():
    numero_computador = random.randint(1,5001)

    return numero_computador

def jogada_jogador():
    numero_jogador = int(input('Digite o número que deseja: '))
    print('='*35)
    return numero_jogador


while True:

    print('='*35) 

    esc_computador = computador()
    esc_jogador = jogador()

    numero_jogador = jogada_jogador()
    numero_computador = jogada_computador()
    
    print(f'O computador escolheu {esc_computador} e o número {numero_computador}')

    resultado = numero_computador + numero_jogador
    print(f'A soma das escolha é igual a: {resultado}')

    print('='*35)

    if (esc_jogador == esc_computador):
        print('Joguem novamente!')
        pass            

    if (esc_jogador == 'par' ) and (esc_computador == 'ímpar'):
        if (resultado % 2 == 0):
            print('Você venceu!')
            jogador_vitorias += 1
        else:
            print('O computador venceu!')
            pc_vitorias += 1

    if (esc_jogador == 'ímpar' ) and (esc_computador == 'par'):
        if (resultado % 2 != 0):
            print('Você Venceu!')
            jogador_vitorias += 1
        else:
            print('O computador venceu!')
            pc_vitorias += 1
    
    print('-'*35)

    print(f'Vitorias do jogador: {jogador_vitorias}')
    print(f'Vitorias do computador: {pc_vitorias}')

    print('-'*35)

    esc_jogador = input('Você deseja jogar novamente? (s/n)')
    if esc_jogador in ['SIM', 'Sim', 'sim', 's']:
        pass
    elif esc_jogador in ['NAO', 'Nao', 'nao', 'n']:
        print(' Obrigado por jogar!')                   
        if jogador_vitorias>pc_vitorias:
            print(' Você venceu o jogo!')
        elif jogador_vitorias == pc_vitorias:
            print(' O jogo empatou!')
        else: 
            print(' O computador venceu o jogo!')    
        break
    else:
        break