import time
import random

print("=" * 20)
print("Jogo de Impar ou Par")
print("=" * 20)

while True:
    jogador = int(input("Escolha um numero: "))

    print("O computador esta escolhendo um numero...")
    computador = random.randint(0, 10)
    time.sleep(1.5)

    resultado = (jogador+computador) % 2

    if resultado == 0:
        print("voce ganhou! :D")
        break
    else:
        print("EROOOOOUUUUU!")
