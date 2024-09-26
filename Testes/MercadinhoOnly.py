import time 

print("=" * 31)
print("Bem vindo ao MercadinhoOnly! :D")
print("=" * 31)

Cesta_de_Compras = list()

while True:
    Produto = str(input("Nome da Mercadoria: "))
    preco = int(input("Preço do produto: "))
    Cesta_de_Compras.append(Produto)
    Cesta_de_Compras.append(preco)
    time.sleep(1)
    esc = str(input("Deseja continuar a compra [S/N]: "))
    if esc != "S" or esc != "SIM" or esc != "sim" or esc != "s":
        break
print("=" * 20)
print(Cesta_de_Compras)
print("=" * 20)