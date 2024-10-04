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
    pagamento = float(input("Digite o seu pagamento do mês:"))
    newsaldo = conta['saldo'] + pagamento
    print("Atualizando seu saldo!")
    time.sleep(1)
    print(f"Atualizado! Seu novo saldo é {newsaldo}")
    
    newsaldo = Verificar_Saldo(conta)
    
    return newsaldo












print("=" * 20)
print("Banco IA")
print("=" * 20)

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
        Depositar_Dinheiro(conta)

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

'''
#======================================================================================#










