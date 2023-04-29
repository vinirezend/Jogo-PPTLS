import random

def jogar():
    #DIALOGO
    print('Olá! Eu sou o Dr. Sheldon Cooper.\n Seja bem vindo' )

    nome = input("Qual seu nome: ")

    while True:
        resposta = input('\nImagino que seja um prazer me conhecer. Hoje jogaremos Pedra, Papel, Tesoura, Lagarto e Spock.\n Você sabe jogar?: ')
        if resposta.lower() in ['sim', 'claro', 'sei', 's', 'logico', 'lógico', 'claro que sei']:
            print('\nIsso foi uma surpresa. Então vamos jogar!\n')
            break
        elif resposta.lower() in ['não', 'não sei', 'claro que não','nao', 'nao sei', 'claro que nao', 'n']:
            print('\n Imaginei. Vou te explicar:\n O jogo se chama "Pedra, papel, tesoura, lagarto, Spock".\n É muito simples. Olhe:\n\n tesoura corta papel,\n papel cobre pedra, \n pedra esmaga lagarto, \n lagarto envenena Spock, \n Spock esmaga tesoura, \n tesoura decapita lagarto, \n lagarto come papel, \n papel refuta Spock, \n Spock vaporiza pedra, \n e como sempre, pedra quebra tesoura.\n\n Agora vamos Jogar!!\n')
            break
        else:
            print('\nVai ser mais dificil do que pensei. Vamos começar de novo.')

    #JOGO
    opcoes = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
    pontuacao = {'jogador': 0, 'sheldon': 0}


    while pontuacao['jogador'] < 3 and pontuacao['sheldon'] < 3:

        jogada_jogador = input(" Escolha sua jogada (pedra, papel,tesoura,lagarto ou spock): ").lower()
        jogada_computador = random.choice(opcoes)

        if jogada_jogador not in opcoes:
            print("Imaginei que você erraria alguma coisa, tenta de novo!")
            continue

        print(f"\n Jogador: {jogada_jogador.capitalize()} \n Sheldon: {jogada_computador.capitalize()}")


        if jogada_jogador == jogada_computador:
            print("Não acredito que você pensa igual a mim. Vamos de novo!\n")
        elif jogada_jogador == 'pedra' and jogada_computador == 'tesoura' or \
             jogada_jogador == 'pedra' and jogada_computador == 'lagarto' or \
             jogada_jogador == 'papel' and jogada_computador == 'spock' or \
             jogada_jogador == 'papel' and jogada_computador == 'pedra' or \
             jogada_jogador == 'tesoura' and jogada_computador == 'papel' or \
             jogada_jogador == 'tesoura' and jogada_computador == 'lagarto' or \
             jogada_jogador == 'lagarto' and jogada_computador == 'spock' or \
             jogada_jogador == 'lagarto' and jogada_computador == 'papel' or \
             jogada_jogador == 'spock' and jogada_computador == 'tesoura' or \
             jogada_jogador == 'spock' and jogada_computador == 'pedra':
            pontuacao['jogador'] +=1
            print(f"\nJogador venceu! Pontuação atual: {nome} {pontuacao['jogador']} x {pontuacao['sheldon']} Sheldon")
        else:
            pontuacao['sheldon'] +=1
            print(f"\nSheldon venceu!Pontuação atual: {nome} {pontuacao['jogador']} x {pontuacao['sheldon']} Sheldon")
            
    else:
        print('O jogo acabou')


if __name__ == '__main__':
    jogar()