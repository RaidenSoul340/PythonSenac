#-------------------------------------#

#for i in range(1, 11):
    #print(i)
'''
Imprimir de 1 a 10.
'''
#-------------------------------------#

#soma = 0

#for i in range(1, 51):
    #soma += i
    #print(soma)

'''
Vai somar todos os numeros de 1 a 50 dando o resultado de 1275.
'''

#-------------------------------------#

#n = int(input("Digite um numero: "))

#for numeros in range(0, 11): 
    #print(f"{n} x {numeros} = {n*numeros}")

'''
Vai multiplicar todos os numero de 0 a 10 pelo numero que for escolhido no 'n'
'''

#-------------------------------------#

#for i in range(1, 21):
    #raiz = i % 2
    #if raiz == 0:
        #print(i)

'''
Vai printar apenas o numeros pares.
'''

#-------------------------------------#

#frase = ("Python é divertido!")
#soma = 0

#for letra in frase:
    #if letra != " ":
        #soma += 1
        
#print(soma)

'''
Imprimir o numero de palavras sem contar os espaços.
OBS: As vezes é bom pensar fora da caixinha e arrumar outros meios
'''

#-------------------------------------#

#numeros = [1, 2, 3, 4, 5]

#for inverso in numeros:
    #numeros.reverse()
    #NV_lista = [numeros]
#print(numeros)

'''
Vai imprimir uma lista com os numeros inversos 5, 4, 3, 2, 1.
'''

#-------------------------------------#

#def eh_quadrado_perfeito(n): # Função def vai verificar se um número é um quadrado perfeito
    #raiz = int(n**0.5)
    #return raiz * raiz == n


#for i in range(1, 101):  #Loop para encontrar e imprimir quadrados perfeitos de 1 a 100
    #if eh_quadrado_perfeito(i):
        #print(i)

#-------------------------------------#

#frase =  str(input("Digite uma frase: ")).lower()
#vogais = "aeiou"
#consoantes = "bcdfghjklmnpqrstvwxyz"
#contador = 0
#contadorCon = 0

#for letra in frase:
    #if letra in vogais:
        #contador +=1
        
    #if letra in consoantes:
        #contadorCon +=1
        
#print(f"Há {contador}, vogais na frase.")
#print(f"Há {contadorCon}, consoantes na frase.")

'''
Vai contar e trazer todas as vogais de uma frase ou letra.
Vai contar e trazer todas as consoantes de uma frase ou letra.
'''

#-------------------------------------#

#def eh_palindromo(num): # Função para verificar se um número é palíndromo
    #return str(num) == str(num)[::-1]


#inicio = int(input("Digite o numero de começo: "))
#fim = int(input("Digite o ultimo numero: "))


#for num in range(inicio, fim + 1):  # Loop para encontrar e imprimir números palíndromos no intervalo
    #if eh_palindromo(num):
        #print(num)

'''
Descobrir numeros polidromos aonde ira começar e onde ira termina

'''

#-------------------------------------#

#import random
#import time

#print("=" * 18)
#print("Jogo de Advinhação")
#print("=" * 18)

#time.sleep(1)
#print("Computador está escolhendo um numero de 0 a 20")
#computador = random.randint(0, 20)
#time.sleep(1)


#while True:
#    palpite = int(input("Digite seu palpite: "))
#    
#    if palpite > computador:
#        print("O número escolhido pelo computador é menor!")
#        
#    elif palpite < computador:
#        print("Passou longe meu patrão! É maior que o palpite!")
#    
#    elif palpite == computador:
#        print("Você acerto :D!")
#        break
#print("Parabéns pela sua vitoria!")

#------------------------------------------------#
print("=" * 15)
print("Mercado Online")
print("=" * 15)

def adicionar_item(compras):
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
            compras.remove(item)
            print(f"'{item}' removido da lista.")
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







