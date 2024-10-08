print("=" * 15)
print("Mercado Online")
print("=" * 15)

def adicionar_item(compras): #recebe
    while True:
        item = input("Digite o item que deseja adicionar (ou 'sair' para terminar): ")
        if item.lower() == 'sair':
            break
        compras.append(item)
        print(f"'{item}' adicionado à lista.")

def remover_item(compras):
    while True:
        if not compras:
            print("A lista está vazia, não há itens para remover.")
            break
        item = input("Digite o item que deseja remover (ou 'sair' para terminar): ")
        if item.lower() == 'sair':
            break
        if item in compras:
            compras.remove(-1)
        else:
            print(f"'{item}' não está na lista.")
                
def mostrar_lista(compras):
    print("Lista de compras:")
    for item in compras:
        print(f"- {item}")
        

while True:
    compras = []
    print("""
        |=================|
        |1-Adcione um item|
        |2-Remover item   |
        |3-Exibir lista   |
        |4-Sair           |
        |=================|
        """)

    esc = input("Escolha uma opção: ")

    if esc == '1':
        adicionar_item(compras)
    elif esc == '2':
        remover_item(compras)
    elif esc == '3':
        mostrar_lista(compras)
    elif esc == '4':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
