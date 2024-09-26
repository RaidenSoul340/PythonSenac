salario = float(input("Digite o valor do seu salario atual: "))
emprestimo = float(input("Digite o valor do emprestimo desejado: "))

calculo1 = (salario*0.50)

calculo2 = (salario*0.75)
 
if emprestimo <= calculo1:
    print("Seu emprestimo foi aprovado! :D")
    
elif emprestimo <= calculo2:
    print("Seu salario esta em analise! :V")
    
else:
    print("seu salario não foi aprovado! >:/")