#==========================#
#imutaveis

#tupla = (1, 2, 3, "quatro")
#print(tuple[0]) #Output: 1
#print(tupla[3]) #Output: quatro
#==========================#
#tupla = (1, 2, 3)
#a, b, c = tupla

#print(a)#Output: 1
#print(b)#Output: 2
#print(c)#Output: 3
#==========================#
#tupla = (1, 2, 3)
#print(2 in tupla)#Output: True
#print(4 in tupla)#Output: False
#==========================#
#tupla = (1, 2, 3, 2, 3, 3)
#print(tupla.count(2)) #Output: 2
#print(tupla.count(3)) #Output: 3
#print(tupla.count(1)) #Output: 1
#print(tupla.count(4)) #Output: 0
#==========================#
        #Exercicio 01:
        
cores = ("Vermelho", "Verde", "Azul")
print(cores[0])
print(cores[-1])
cores = ("Vermelho", "Verde", "Azul",)
cores2 = ("Amarelo", "Roxo")
cores3 = cores + cores2
print(cores3)
cor1, cor2, cor3, cor4, cor5 = cores3

print(cor1)
print(cor2)
print(cor3)

'''
Tuplas são imutaveis logo não podem ser alteradas
'''