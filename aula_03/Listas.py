#======================================#
#declarando lista vazia!

#lista_01 = [1, "2", 3] #Criando a lista
#print(type(lista_1), lista_1)

#Declaração explícita da lista

#lista_02 = list((1, "2", 3))
#print(lista_2)

#Declaração implícita

#lista_03 = ["C", 4.65, True, "True", "Vamos aprender", ["outra", "lista", "interna"], lista_02]
#print(lista_03)

#lista_04 = ["primeiro", "segundo", "terceiro"]
#print(lista_04)
#======================================#

#======================================#

  #========#Fatiando Listas#========#
  
#Executando um print por vez!

#print(lista_03)
#print(lista_03[2:6:2])
#print(lista_03[:3])
#print(lista_03[-1:])
#print("Imprimindo de dois em dois ", lista_03[::2])
#print(lista_03[: : ])
#print(len(lista_03))

#================================================#
            #METODOS DE LISTA 
            
            
#print(lista_01)
#lista_01.append("java")
#lista_01.append("Ruby")
#lista_01.append("python")
#lista_01.append("PHP")
#lista_01.append("C#")

#print(lista_01)

#inserir elementos em uma posição especifica

#lista_01.insert(2, "C++")
#print(lista_01)

#Removendo elementos de uma lista

#lista_01.remove("java")
#print(lista_01)

#indice = lista_01.index("PHP")
#print(indice)

#Remove im elemento pelo seu indice 
#del(lista_01[indice])
#print(lista_01)

#print("Lista Original: ", lista_04)

#invertendo a lista
#lista_04.reverse()

#Ordenando a lista
#lista_04.sort()
#print("lista Original: ", lista_04)

#Comprimento da lista

#print(lista_01, len(lista_01), "Elementos")
#print(lista_02, len(lista_02), "Elementos")
#print(lista_03, len(lista_03), "Elementos")
#print(lista_04, len(lista_04), "Elementos")

#=================================================#
              #Exercicio 01:
minhaLista = [76, 92,3, "oi", True, 4, 76]
#minhaLista.insert(6, "pera")
#minhaLista.insert(7, 76)
#minhaLista.insert(3, "gato")
#minhaLista.insert(0, 99)

#print(minhaLista)
indice = minhaLista.index("oi")
print(indice)

#minhaLista.remove(True)
#print(minhaLista)
#=================================================#
              #Exercicio 01:
        
#frutas = ["Maça", "Banana", "Laranja"]
#frutas.append("Uva")
#frutas.remove("Banana")
#print(frutas[1])
#frutas.reverse()
#print(frutas)
