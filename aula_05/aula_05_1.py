'''
Funçao é o bloco de código que realiza uma tarefa especifica.

VANTAGENS:

#Reutilização de Código:

'''

#=================================#
#Sintaxe Básica

#def  nome_da_funcao(parametros):
#    #bloco de código
#    return resultado
    
#=================================#
            #Exemplo 01:

#def saudacoes():
#    print("Olá, bem vindo(a) à aula de função em python!")
#    return
    
#saudacoes()

#=================================#
            #Exemplo 02:

#def saudacoes(nome): #'nome' é um parametro
#    print(f"Olá, {nome}")

#saudacoes(input("Seu nome: ")) #A pessoa insere um nome e ele é printado

#=================================#
            #Exemplo 03:

#def somar(a, b): #Mais de um parâmetro
#    return a+b

#n1 = float(input("Digite um numero: "))
#n2 = float(input("Digite outro valor: "))

#resultado = somar(10, 20) soma os valores totalizando 30
#resultado = somar(n1, n2)
#print(resultado)

#=================================#
            #Exemplo 04-1:

#def checar_numero(n): #Parametro n definido
#    if n > 0:
#        return "Positivo" #Positivo

#    elif n < 0:
#        return "Negativo" #Negativo

#    else:
#        return "Zero" #ira retorna o valor 0

#print(checar_numero(10))
#n = float(input("Digite um numero: ")) # Pede um numero
#resultado = checar_numero(n) #Resultado vai puxar a função 'checar_numero()' com o n dentro
#print(resultado) # printa Resultado

#=================================#
            #OBSERVAÇÃO

#Escopo de Variáveis: Variáveis definidas dentro de uma função só existem dentro dela.

#Escopo Global: Variáveis definidas de qualquer função podem ser acessadas em qualquer parte do código

#=================================#

#=================================#
            #Exemplo 05:

#global_var = 100

#def exemplo_escopo():
#    local_var = "Estou dentro da função"
#    print(local_var)
#    print(global_var)

#exemplo_escopo()
#print(local_var)

'''
A variavel 'local_var' não existe e nem foi definida fora ou dentro logo ira da erro até ser definida.
'''

#=================================#
            #Exemplo 06:

#def exibir_nome_idade(nome, idade):
#    print(f"Nome: {nome}, Idade: {idade}")

#nome = input("Digite seu nome: ")
#idade = input("Digite sua idade: ")

#exibir_nome_idade(nome, idade)

#=================================#
            #Exemplo 07:

'''
Argumentos Arbitrários (*args e **kwargs)
'''
#args: Recebe mútiplos argumentos como uma tupla.

#def somar_todos(*args):
#    return sum(args)

#print(somar_todos(1, 2, 3, 4, 5)) #Saida 15


#---------------------------------#

# **kwargs: Recebe múltiplos argumentos nomeados como um dicíonario.
#def exibir_Detalhes(**kwargs):
#    for chaves, valor in kwargs.items():
#        print(f"{chaves}: {valor}") #'Chave' vai ta recebendo a variavel, e 'valor' seu valor
        
#exibir_Detalhes(nome='Calor', idade=30, cidade='São Paulo', telefone=819988775566)

#=================================#
            #Exemplo 06:

#def soma_pares(numeros):
#    soma = 0
#    i = 0
#    while i < len(numeros):
#        if numeros[i] % 2 ==0:
#            soma +=numeros[i]
#        i += 1
#    return soma

#print(soma_pares([1, 2, 3, 4, 5, 6])) #saida 12

#=================================#
            #Exemplo 07:

def obter_detalhes_pedido(): #Simula a obtenção de detalhes de um pedido
    pedido = {
        "item" : "Notebook",
        "preco" : 1200.00,
        "quantidade" : 2
    }
    print("detalhes do pedido obtido")
    return pedido

def calculador_preco_total(pedido):
    #Calculadora o preço total do pedido
    preco_total = pedido['preco'] * pedido['quantidade']
    print(f"Preço total calculado: R${preco_total}")
    return preco_total

def  enviar_confirmacao(pedido, preco_total):
    #Simulada o envio de uma confirmação de pedido
    print(f"Confirmação enviada para {pedido['quantidade']} {pedido['item']}.")
    print(f"Valor total a ser pago: R${preco_total}")
    
def processar_pedido():
    #Chaves as funções auxiliares para processar o pedido
    pedido = obter_detalhes_pedido()
    preco_total = calculador_preco_total(pedido)
    enviar_confirmacao(pedido, preco_total)
    
#chamando a função principal
processar_pedido()














