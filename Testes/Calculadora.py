import time
nome = str(input("Digite seu nome: "))

print('=' * 83)
print("Prazer {}, seja bem vindo ao nosso sistema avançado de educação!".format(nome))
print('=' * 83)
while True:
    
    n1 = float(input("Escolha um numero: "))
    n2 = float(input("Escolha outro numero: "))
    
    print("""
        #=========Calculadora=========#
        
        1-Soma;
        
        2-Subtração
        
        3-Multiplicação
        
        4-Divisão
        
        #=============================#
        """)

    esc = int(input("Escolha uma das opções da tabela: "))

    while True:

        if esc == 1:
            print("A soma dos numeros é {}".format(n1+n2))
            break
        time.sleep(1)
        if esc == 2:
            print("A subtração dos numeros é {}".format(n1-n2))
            break
        time.sleep(1)
        if esc == 3:
            print("A multiplicação dos numeros é {}".format(n1*n2))
            break
        time.sleep(1)
        if esc == 4:
            print("A divisão dos numeros é {}".format(n1/n2))
            break
        time.sleep(1)
        
        if esc >= 5:
            print("Valor não existe tente novamente")
            break
        time.sleep(1)
    else: 
        print("Sistema encerrado volte sempre!")