
#======================================#
#sequenciar palavras chave
#Atenção: Usem o print para retorna p valor das variaveis!!
#declarando uma string:

mensagem = "Hello, World"

#======================================#
#Concatenando String:

#primeito_nome = "joao"
#sobrenome =  "Silva"
#nome_complemento = primeito_nome + " " + sobrenome
#print(nome_complemento)

#======================================#

#Acessando caracteres individuais em uma string:

#primeito_caractere = mensagem[0]
#ultimo_caractere = mensagem[-1]
#print(primeito_caractere)
#print(ultimo_caractere)

#======================================#

#Encontrando o comprimento de uma string:

#mensagem = "Hello, world!"
#comprimento = len(mensagem)
#print(comprimento)

#======================================#

#Convertendo uma string para letras maiúsculas ou minúsculas

#maiuscula = mensagem.upper()
#minuscula = mensagem.lower()
#print(maiuscula)
#print(minuscula)

#======================================#

#dividindo uma string em substrings com base em uma delimitação

#palavras = mensagem.split(",")
#print(palavras)

#======================================#

#Verificando se uma substring está presente em uma string:

#if "world" in mensagem:
    #print("A substring 'world' está presente na mensagem.")
    
#======================================#

#Substituindo caracteres em uma string:

#nova_mensagem = mensagem.replace("World", "python")
#print(nova_mensagem)

#======================================#

#Obtendo um conjunto especifico de caracteres:
#frase = "Hello, world"
#letras_pares = frase[::2] #Retorna "Hlo ol!"
#print(letras_pares)

#======================================#

#Removendo espaços em branco de uma string: 

#frase = "  Hello, word!    "
#sem_espaços = frase.strip() #Retorna "Hello, world!"
#print(sem_espaços)

#======================================#
            #Desafio 01:
            
frase = "Estrutura de Dados em Python"
print(frase.upper())
posicao = frase.find("Dados") #Comando 'find' é usado para encontrar a localização.
print(posicao)
nova_palavra = frase.replace("Python", "Java")
print(nova_palavra)
frase_palavras = frase.split(" ")
print(frase_palavras)