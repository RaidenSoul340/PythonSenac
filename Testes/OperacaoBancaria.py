import time
#==============================================#
def Detalhes_Conta(nome, idade, saldo):
    banco = {
        "nome" : nome,
        "idade" : idade,
        "saldo" : saldo
    }
    return banco

'''
Detalhes_Trás as informações do usario
'''
#=============================================#

def add_conta(nome, idade, saldo):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    saldo = float(input("Digite seu saldo atual: "))
    time.sleep(1)
    print("Sua conta foi criada :D")
    
    print(f"Seja bem-vindo {nome}, seu saldo atual é R${saldo}, sua idade atual é {idade}")
    time.sleep(1)
    
    return Detalhes_Conta(nome, idade, saldo)

'''
Detalhes_Conta esta dentro de add_conta para que possa receber as informações
add_conta vai jogar as informações do usuario para o banco de dados 'banco'
'''
#==============================================#

def Verificar_Saldo(conta):
    print(f"Seu saldo atual é: R${conta['saldo']}")

'''
Foi criada uma variavel como o nome 'conta' e foi definido o que ele vai puxar de conta
'''
#==============================================#

def Depositar_Dinheiro(conta):
    pagamento = float(input("Digite o seu pagamento do mês: "))
    conta['saldo'] += pagamento 
    print("Atualizando seu saldo!")
    time.sleep(1)
    print(f"Atualizado! Seu novo saldo é R${conta['saldo']}")
    
    return conta

'''
Quando o cliente quer depositar dinheiro, ele vai digitar o valor que ele vai ser depositado
com isso é somado e logo em seguida atualizado na 'conta'
'+=' É uma forma abreviada de escrever uma operação de adição e atribuição ao mesmo tempo.
'''
#==============================================#

def Sacar_Dinheiro(conta):
    saque = float(input("Digite o valor do seu saque: "))
    if saque <= conta['saldo']:
        conta['saldo'] -= saque
        print("Saque realizado com sucesso!")
        time.sleep(1)
        print(f"Seu novo saldo é R${conta['saldo']}")
    
    elif saque > conta['saldo']:
        print("Saldo insuficiente!")
        
    else:
        print("Ocorreu um erro!")
    
    return conta

'''
Quando o cliente quer sacar dinheiro, ele vai digitar o valor que ele vai ser sacado
com isso é subtraido e logo em seguida atualizado na 'conta'
'-=' é uma forma abreviada de escrever uma operação de subtração e atribuição ao mesmo tempo.
'''

#==============================================#

print("=" * 20)
print("Banco IA")
print("=" * 20)

conta = None

while True:

    print("""
        1- Criar Conta.
        2-Verificar saldo.
        3-Depositar dinheiro.
        4-Sacar dinheiro.
        5-Encerrar o Atendimento
        """)
    
    esc = input("Digite o digito de qualquer uma das opções acima: ")
    time.sleep
    
    if esc == '1':
        conta = add_conta('nome', 'idade', 'saldo')
        print(conta)
        #Mostrando na tela as informações do usuario
    
    elif esc == '2':
        Verificar_Saldo(conta)

    elif esc == '3':
        if conta:
            conta = Depositar_Dinheiro(conta)
            
    elif esc == '4':
        if conta:
            conta = Sacar_Dinheiro(conta)
    
    elif esc == '5':
        print("Encerrando o Atendimento!")
        time.sleep(1)
        break

#======================================================================================#
                                        #Observações                                                    

'''
1- Foi criada uma função Detalhes_Conta ela recebe um dicionario chamado 'banco',
vai que ele recebe as variaveis 'nome', 'idade' e 'saldo' e depois essas informações
vão ser armazenadas através do return.

2- A função com o nome 'add_conta' ela foi criada para que as informações do 'cliente',
foi usado o 'time.sleep(1)' para antes de puxar os outros print esperar um tempo de 1s.
Depois mostra na tela as informações do 'cliente'.

3- A função Verificar_saldo ira printa apenas o 'saldo' do cliente, através da variavel,
'conta' que ta recebendo a função 'add_conta'

4- A função Depositar_Dinheiro vai pedir para o cliente digitar o valor que ele vai
ser depositado e logo em seguida somado e atualizado na variavel 'conta'.

5- A função Sacar_Dinheiro vai pedir para o cliente digitar o valor que ele vai ser sacado
e logo em seguida subtraido e atualizado na variavel 'conta'.

'''
#======================================================================================#
