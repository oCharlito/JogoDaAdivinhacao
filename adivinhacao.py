print("Bem-vindo ao jogo da adivinhação!")

numero_secreto = 42
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print(f"Tentativa {rodada} de {total_tentativas}")

    palpite = int(input("Tente adivinhar o número secreto. Arrisque um palpite.\n"))

    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break
    elif palpite > numero_secreto:
        print("Errou! Você chutou alto. Tente outra vez!")
    else:
        print("Errou! Você chutou baixo. Tente outra vez!")

if rodada == total_tentativas and palpite != numero_secreto:
    print(f"Suas {total_tentativas} tentativas acabaram. O número secreto era {numero_secreto}.")