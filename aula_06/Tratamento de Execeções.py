'''
Tratamento de Execeções

Exceções são eventos que ocorrem durante a execução de uma programa
que interrompem o fluxo normal das instruções

Robustez: Permitem que o programa lide com situações inesperadas
sem parar abruptamente

Clareza: Ajudam a identificar e isolar problemas no código

Manutenção: Facilitam a manutenção do código ao fornecer mecanismo claros de
tratamento de erros.
'''

#============================================================================#
'''
Exemplos comuns de exceções

ZeroDivisionError = Ocorre quando se tenta dividir um número por zero.

TypeError: Ocorre quando uma operação é aplicada a um objeto de tipo Inadequado.

ValueError: Ocorre quando uma operação recebe um argumento com o tipo certo, mas
valor inapropriado.

FileNotFoundError: Ocorre quando se tenta abrir um arquivo que não existe
'''
#============================================================================#

#Bloco try e except:

'''
O bloco 'try' permite que você teste um bloco de código quando a erros

O bloco 'except' permite lidar com o erro.
'''

#Sintaxe Básica:

#try:
    #O código que pode causar uma exceção

#except TipoDaExceção:
    # O código que será executado se ocorrer a exceção

#else:
    #Código que será executado se nenhuma exceção ocorrer

#============================================================================#
                                    #Exemplo_01:

#try:
#    resultado = 10/2

#except ZeroDivisionError:
#    print("Erro: Divisão por zero não é permitida.")

#else: print(f"O resultado é {resultado}")

#============================================================================#
                                    #Exemplo_02:

#Bloco finally:
'''
O bloco finally é executado independentemnte se a exceção ocorreu ou não.
OBS: É normalmente usado para liberar recursos externos(arquivos, conexão de rede, etc)
'''

#try:
    #O código que pode causar uma exceção

#except TipoDaExceção:
    # O código que será executado se ocorrer a exceção

#finally:
    #Código que será sempre executado

#try:
#    arquivo = open("dados.txt", "r")
#    conteudo = arquivo.road()

#except FileNotFoundError:
#    print("Erro: Arquivo não encontrado")

#finally:
#    print("Operação finalizada.")

#============================================================================#
                                    #Exemplo_03:

#Uso combinado dos blocos
'''
É possível combinar todos os blocos para um tratamento de exceções mais completo.
'''

#try:
#    num = int(input("Digite um número: "))
#    resultado = 100 / num

#except ValueError:
#    print("Erro: Você deve digitar um número inteiro.")

#except ZeroDivisionError:
#    print("Erro: Divisão por zero não é permitida.")

#else:
#    print(f"O resultado é {resultado}")

#finally:
#    print("Obrigado por usar o programa")

#============================================================================#

#Levantando Exceções: 

'''
ÀS vezes, você pode querer gerar(levantar) uma exceção em seu código, quando ocorrer uma
condição específica.
'''

#Uso do raise:
'''
A instrução raise permite que você force uma exceção a ocorrer
'''

#raise TipoDaExceção("Mensagem de erro") # type: ignore

#exemplo:

#def verifica_idade(idade):
#    if idade <18:
#        raise ValueError("Idade deve ser maior ou igual a 18.")
#    else:
#        print("Entrada permitida.")

#try:
#    verifica_idade(18)

#except ValueError as e:
#    print(e)

#============================================================================#

#Criação de Exceções Personalizadas:

'''
Se nenhuma das execeções enbutidas descrever adequadamente o erro que você quer sinalizar,
você pode criar suas próprias exceções.
'''

#Exemplo:

#class SaldoInsuficienteError(Exception):
#    """Exceção levantada quando o saldo é insuficiente para realizar uma transação."""
#    pass

#def sacar(valor, saldo):
#    if valor > saldo:
#        raise SaldoInsuficienteError("Saldo insuficiente para sacar o valor solicitado")
#    saldo >=valor
#    return saldo

#try:
#    saldo_atual = sacar(1500, 1000)
#except SaldoInsuficienteError as e:
#    print(e)

'''
Para que fazer exceções personalizadas?:

Especificidade: Fornece informações mais específicas sobre o erro.

Organização: Ajuda a organizar melhor o código de tratamento de erros.

Legibilidade: Torna o código mais legível e fácil de entender
'''

#============================================================================#
                                    #Resumo

'''
Exceções são eventos anormais que ocorrem durante a execução de um programa
'''

#O bloco 'try' permite que você teste um bloco de código quanto a erros.

#O bloco 'except' permite lidar com erros.

#O bloco 'else' é executado se nenhuma exceção ocorrer.

#O bloco 'finally' é executado independentemente do resultado bloco 'try'.

#O instrução 'raise' é usada para gerar uma exceção.

#Você pode criar execeção personalizadas definindo uma nova classe herda de 'Exception'.