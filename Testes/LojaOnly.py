print("""
    |=================|
    |1-Adcione um item|
    |2-Remover item   |
    |3-Exibir lista   |
    |4-Sair           |
    |=================|
    """)

def adicionar(add_item):
    compras.append(add_item)
    compras = [add_item]

while True:
    esc = input("Digite um valor que esteja na tabela: ")
    
    compras = []

    if esc == '1':
        while True:
            add_item = input("Digite o item que deseja adicionar(caso queira parar digite 'sair'): ")
            compras.append(add_item)

            if add_item.lower() == 'sair':
                compras.pop(-1)
                break

    elif esc == '2':
            remove_item = input("Deseja excluir o item que você adicionou?(digite 'sim' ou 'nao'): ")

            if remove_item.lower() == 'sim':
                if compras:
                    print("removido com sucesso!")
                    compras.pop()
                    
            elif remove_item == 'nao':
                print('')
                
    elif esc == '3':
        print(compras)
        break
        
    if esc == '4':
        print("lista finalizada!")
        print(compras)
        break
