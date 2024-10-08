'''
Principais conceitos da POO:

Classes: são tipos de dados definidos pelo desenvolvedor que atuam como um modelo para objetos. 
Pra não esquecer mais: Classes são fôrmas de bolo e bolos são objetos :wink:

Objetos: são instâncias de uma Classe. Objetos podem modelar entidades do mundo real (Carro, Pessoa, Usuário) 
ou entidades abstratas (Temperatura, Umidade, Medição, Configuração).

Métodos: são funções definidas dentro de uma classe que descreve os comportamentos de um objeto. Em Python, 
o primeiro parâmetro dos métodos é sempre uma referência ao próprio objeto.

Atributos: são definidos na Classe e representam o estado de um objeto. Os objetos terão dados armazenados nos campos de atributos. 
Também existe o conceito de atributos de classe, mas veremos isso mais pra frente.

Encapsulamento: Protege os dados de uma classe, permitindo acesso apenas através de métodos específicos.

Abstração: Simplifica a complexidade ao focar nos aspectos essenciais de um objeto

Herança: Permite que uma classe derive características de outra, promovendo a reutilização de código

Polimorfismo: Habilita métodos a terem diferentes comportamentos baseados no objeto que os invoca.

'''
#============================================================================#

#Sintaxe Básica:

#class NomeDaClasse:
#    #definição da classe
#    pass

#============================================================================#
                                    #Exemplo_01:

#lass Pessoa:
#    pass

#pessoa1 = Pessoa()
#pessoa2 = Pessoa()

#============================================================================#
                                    #Exemplo_02:

'''
Atributos de Instância

Atributos de instância são variáveis que pertencem a cada objeto.

Eles são geralmente definidos dentro do método.
__init__(construtor)
'''

#class Pessoa:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade

#pessoa1 = Pessoa("Maria", 30)
#print(pessoa1.nome) #Saída: Maria
#print(pessoa1.idade) #Saída: 30

#pessoa2 = Pessoa("Chico", 20)
#print(pessoa2.nome) #Saída: Chico
#print(pessoa2.idade) #Saída: 20

#============================================================================#
                                    #Exemplo_03:

'''
Métodos são funções definidas dentro de uma classe que descrevem os comportamentos de um objeto
'''
import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
    
    def AnoATual(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual

    def  ano_nascimento(self):
        ano_atual = self.ano_nascimento()
        ano_nascimento = ano_atual - self.idade
        return ano_nascimento

pessoa1 = Pessoa("Maria", 30)
#print(pessoa1.nome) #Saída: Maria
#print(pessoa1.idade) #Saída: 30
#print(pessoa1.nascimento) #Saída: 1994

pessoa1.apresentar()
pessoa1.AnoATual()
print(f"Eu nasci em {pessoa1.ano_nascimento()}.")

'''
Foi criado 'AnoATual()' onde puxa atraves do import datetime, além de usar '.year' que trás ano do calendario.
'ano_nascimento()' vai realizar o calculo do ano de nascimento, ano_atual vai iguala ano_nascimento fazendo receber o ano atual.
Logo após isso ano_nascimento vai subtrair ano_atual - self.idade que é a idade da pessoa

'''
#============================================================================#





























