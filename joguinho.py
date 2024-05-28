
import os
import time

def limparTela():
    os.system("cls")

def aguarde(segundos):
    time.sleep(segundos)

def palavraChaveLetras(palavraChave, letrasAcertadas):
    palavraSecreta = ''
    for letra in palavraChave:
        if letra in letrasAcertadas:
            palavraSecreta += letra
        else:
            palavraSecreta += '*'
    print(palavraSecreta)

def jogo_da_forca():
    limparTela()
    print("Bem vindo ao jogo da forca")
    aguarde(1)
    nomeDesafiante = input("Nome do desafiante: ")
    nomeCompetidor = input("Nome do competidor: ")
    limparTela()

    palavraChave = input(f"{nomeDesafiante}, digite a palavra chave: ").upper()
    dica1 = input("Digite a dica 1: ")
    dica2 = input("Digite a dica 2: ")
    dica3 = input("Digite a dica 3: ")
    print("Preparando o jogo...")
    aguarde(2)

    letrasAcertadas = []
    tentativasMax = 6
    numeroAsterisco = len(palavraChave)

    dicas_disponiveis = [dica1, dica2, dica3]
    dicas_utilizadas = 0

    print(f"{nomeCompetidor}, preparado?")
    input("Pressione ENTER para continuar ")
    print("A palavra é: ")
    print("*" * numeroAsterisco)

    while True:
        print("O que deseja fazer? (1) Jogar (2) Pedir dica")
        opcaoJogo = input()

        if opcaoJogo == "1":
            letra = input("Escolha uma letra: ").upper()
            if letra in palavraChave:
                letrasAcertadas.append(letra)
                palavraChaveLetras(palavraChave, letrasAcertadas)
                if set(palavraChave) == set(letrasAcertadas):
                    print(f"Parabéns {nomeCompetidor}! Você acertou a palavra!")
                    break
            else:
                tentativasMax -= 1
                print(f"Vidas: {tentativasMax}/{tentativasMax}")
                if tentativasMax == 0:
                    print(f"Você perdeu! A palavra era {palavraChave}")
                    break
        elif opcaoJogo == "2":
            if dicas_utilizadas < 3:
                print(f"Dica: {dicas_disponiveis[dicas_utilizadas]}")
                dicas_utilizadas += 1
            else:
                print("Você já utilizou todas as dicas disponíveis.")
        else:
            print("Opção inválida!")

    print("Deseja jogar novamente? ")
    jogarDenovo = input("Digite (sim) para jogar novamente ou (sair) para sair: ")
    if jogarDenovo.lower() == "sim":
        jogo_da_forca()
    else:
        print("Obrigado por jogar!")

# Iniciar o jogo
jogo_da_forca()

