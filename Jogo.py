import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
    pontuacao = {'jogador': 0, 'sheldon': 0}

    while True:
        print(f"\nPontuação atual: Jogador {pontuacao['jogador']} x {pontuacao['sheldon']} Sheldon")

        jogada_jogador = input("Escolha sua jogada (pedra, papel,tesoura,lagarto ou spock): ").lower()
        jogada_computador = random.choice(opcoes)

        if jogada_jogador not in opcoes:
            print("Imaginei que você não entenderia, vou repetir!")
            continue

        print(f"Jogador: {jogada_jogador.capitalize()} x Sheldon: {jogada_computador.capitalize()}")

        if jogada_jogador == jogada_computador:
            print("Não acredito que você pensa igual a mim. Vamos de novo!")
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
            print("Jogador venceu!")
            pontuacao['jogador'] += 1
        else:
            print("Computador venceu!")
            pontuacao['computador'] += 1

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente == 'n':
            break

if __name__ == '__main__':
    jogar()