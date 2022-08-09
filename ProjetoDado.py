#tentativa de fazer rolagem de dados, existem erros no qual estou pesquisando para solucionar.
from numpy import random

print('!!! Jogo de dados!!! ')

iniciar_jogo = input('Gostaria de rolar o dado?:\n ')


while iniciar_jogo == 'Sim' or iniciar_jogo == 'S' or iniciar_jogo == 'sim' or iniciar_jogo == 's':
    dado = random.randint(1, 6)
    print('Rolando o dado e o valor foi : ', dado)
    iniciar_jogo = input('Deseja jogar novamente? : ')

    if iniciar_jogo == 'Não' or iniciar_jogo == 'N' or iniciar_jogo == 'não' or iniciar_jogo == 'n':

        print('jogo encerrado, ate a proxima')
        break



else:
    print('Favor digitar sim ou não ')
    iniciar_jogo = input('Deseja jogar novamente? : ')

