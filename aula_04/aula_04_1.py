#Estruturas de Repetição

'''
Permite iterar sobre uma sequência como listas, tuplas, string e dicionarios

Sintaxe básica de um for em Python é:

for 'nome da variavel' in sequecencia:

'''

 #=============================================#  
                    #Exemplo 01:
                    
#frutas = ["maçã", "banana", "laranja"]

#for fruta in frutas:
    #print(frutas)
    
 #=============================================#  
                    #Exemplo 02:
                    
#for i in range(10): #Gera uma sequencia de 0 ate 4. O ultimo numero não aparece
    #print(i) 
    #print(i, i>5, ++i) #Faz a comparação dos numeros que são gerados no i com 0 5 enquanto for menor é False, quando for maior True
 
 #=============================================#  
                    #Exemplo 03:

#soma1 = 0
#for i in range(1, 11): #Sequencia vai começar em 1 e termina em 10
    #soma1 += i
    
#print("A soma de 1 a 10 é: ", soma1) #Vai somar todos os numeros de 1 a 10

 #=============================================#  
                    #Exemplo 04.1:

#palavra = "python"
#for letra in palavra:
    #soma = letra + palavra
    #print(soma.find('p'))  #Trazendo cada palavra como item então é printado 'P-Y-T-H-O-N'

'''
caso seja utilizado o soma.find('p') ele vai buscar onde se encontra o 'p' assim ele trás 0 pra primeiro posição e 1 para segunda posicão do 'p'
'''
#-------------------------------------------------------------#
#palavra = "Python"

#for indice, palavra in enumerate(palavra):
    #if indice == 0:
        #print(f"A letra {palavra}, esta no indice {indice}")
        
#OU

#for i in palavra:
    #print(f"A letra {i} tem o indice {palavra.index(i)}")
    
'''
Vai da numera cada palavra com seu indice e ira mostrar na tela.
'''

#-------------------------------------------------------------#
                    #Exemplo 04.2:

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


