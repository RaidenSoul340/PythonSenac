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

try:
    resultado = 10/2

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

else: print(f"O resultado é {resultado}")




