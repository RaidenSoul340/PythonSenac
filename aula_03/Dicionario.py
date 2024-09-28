#======================================#
#Declarando Dicionario

dic = {}
#print(type(dic))
dic_pernambuco = {"Sport" : 41, "Santa Cruz" : 29, "Nautico" : 21}
#print(dic_pernambuco)

#======================================#

#Adicionando um elemento no dicionario (chaves: valor)
#Onde a chaves é "Salgueiro" e o valor é 1.
#Note que a chave é passada dentro de colchetes, após o nome do dicionario
#dic_pernambuco["Salgueiro"] = 1
#print(dic_pernambuco)

#======================================#

#Buscando o valor com base na chave
#qnt_titulos = dic_pernambuco.get("Sport")
#print(qnt_titulos)
#print("O Sport tem", qnt_titulos, "Titulos")
 
#======================================#

#Remover um elemento com base na chave
#del dic_pernambuco["Salgueiro"]
#print(dic_pernambuco)

#Removendo a chaves e retorna seu valor

#valor = dic_pernambuco.pop("Nautico")
#print("O valor retornado da chave é: ", valor) 
#print(dic_pernambuco)

#======================================#

#Verificar se uma chave existe no dicionario

#print("Santa Cruz" in dic_pernambuco)

#======================================#

#Pegar todas as chaves do dicionario
#print(dic_pernambuco.keys())

#Pegar todos os valores do dicionario
#teste = dic_pernambuco.values()
#print(teste)

#======================================#

dic_paulista = {"Corinthias" : 29, "Santos" : 22, "Palmeiras" : 22}

#removendo e retonando ultimo elemento
#print(dic_paulista.popitem())
#print(dic_paulista)

#======================================#

#Mesclar dois dicionarios

#dic_pernambuco.update(dic_paulista)
#print(dic_pernambuco)

#======================================#

#convertendo um Dicionario em uma lista

#print(list(dic_pernambuco))
#print(list(dic_paulista))

#======================================#
            #Exercicio 01:
            
alunos = {
    "nome" : "Joao", 
    "idade" : 16, 
    "nota" : 8,
}

print(alunos["nome"])
alunos["cursos"] = "Ciência da computação"
del alunos["nota"]
print(alunos)
print("idade" in alunos)