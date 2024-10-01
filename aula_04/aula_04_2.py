#Estrutura de Repetição While

'''
While ira repetir uma função quantas vezes for necessario ate o objetivo ser alcançado
Essa repetição ira ocorrer enquanto for verdadeira, quando se torna falsa sera interrompido
'''

 #=============================================#  
                    #Exemplo 01:

#contador = 6

#while contador >=5:
    #print(contador)
    #contador += 1

 #=============================================#  
                    #Exemplo 02:

#while True:
    #nome = str(input("Digite seu nome (ou 'sair' para parar): "))

    #if nome == 'sair':
        #break
    #print(f"Ola {nome}!")
    
'''
Quando o usuario digitar 'sair' ira interromper codigo consequentemente terminara a repetição do codigo
'''

 #=============================================#  
                    #Exemplo 04:

#import time

#contagem = 10

#while contagem > 0:
    #print(contagem)
    #time.sleep(1)
    #contagem -= 1

#print("Feliz Ano Novo!")

 #=============================================# 
                #Exercicio 01:

#cont = 1

#while cont <= 10:
    #print(cont)
    #cont += 1

#=============================================# 
                #Exercicio 02:

#while True:
    #senha = str(input("Digite uma senha: "))

    #if senha == '1234':
        #break
    #print("senha incorreta")

#=============================================# 
                #Exercicio 03:

#numeros = []

#while True:
    #n = int(input("Digite um numero: "))
    #numeros.append(n)

    #if n == 0:
        #break 
#print(sum(numeros))

#=============================================# 
                #Exercicio 04:

#cont = 2

#while cont <= 40:
    #print(cont)
    #cont += 2

#=============================================# 
                #Exercicio 05:

nomes = []

while True:
    name = input("Digite um nome(Caso queira finalizar digite 'sair/Sair'): ")
    nomes.append(name)

    if name == 'sair':
        nomes.pop(-1)
        break
    
print(nomes)









