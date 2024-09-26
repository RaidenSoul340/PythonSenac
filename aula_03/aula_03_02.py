cupom = str(input("Digite seu cupom: "))

#Primeiro metodo
#=============================================#
#if (cupom == "FUCTURA1" or cupom=="FUCTURA2"):
    #print("Você ganhou 15% de desconto")
 #=============================================#   
    
#Primeiro metodo
#=============================================# 
if cupom == "FUCTURA1":
    print("Você ganhou 15% de desconto! :D")
    
elif cupom == "FUCTURA2":
    print("Você ganhou 10% de desconto! :D")
    
elif cupom == "CUPOM345":
    print("Você ganhou 50% de desconto")
#=============================================#

else:
    print("Você não ganhou o desconto! :3")
    
    '''
    Primeiro Metodo:
    A ulitilização do 'or' faz a identificação de ambos valores, mas caso seja digitado outro nome retornara o 'else'.
    
    Segundo Metodo:
    A utilizaççao do 'elif' além de ser uma boa pratica está servindo como segunda opção de resultado!
    '''