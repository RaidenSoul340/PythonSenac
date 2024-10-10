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
#import datetime

#class Pessoa:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade

#    def apresentar(self):
#        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

#    def AnoATual(self):
#        ano_atual = datetime.datetime.now().year
#        return ano_atual

#    def  ano_nascimento(self):
#        ano_atual = self.ano_nascimento()
#        ano_nascimento = ano_atual - self.idade
#        return ano_nascimento

#pessoa1 = Pessoa("Maria", 30)
#print(pessoa1.nome) #Saída: Maria
#print(pessoa1.idade) #Saída: 30
#print(pessoa1.nascimento) #Saída: 1994

#pessoa1.apresentar()
#pessoa1.AnoATual()
#print(f"Eu nasci em {pessoa1.ano_nascimento()}.")

'''
Foi criado 'AnoATual()' onde puxa atraves do import datetime, além de usar '.year' que trás ano do calendario.
'ano_nascimento()' vai realizar o calculo do ano de nascimento, ano_atual vai iguala ano_nascimento fazendo receber o ano atual.
Logo após isso ano_nascimento vai subtrair ano_atual - self.idade que é a idade da pessoa

'''
#============================================================================#

#Herança
'''
Herança permite que uma classe (subclasse) herda atributos e métodos de outra classe (superclasse)
'''

#class Animal:
#    def __init__(self, nome):
#        self.nome = nome

#    def emitir_som(self):
#        print(f"{self.nome} diz: barulho!")

#class Dono:
#    def __init__(self, dono):
#        self.dono = dono

#    def reclamcao(self):
#        print(f"{self.dono} diz: silencio!")

#class Cachorro(Animal):
#    pass

#class Gato(Animal):
#    pass

#class Pessoa1(Dono):
#    pass

#class Pessoa2(Dono):
#    pass

#dog = Cachorro("Rex")
#cat = Gato("Tom")

#ps1 = Pessoa1("Alex")
#ps2 = Pessoa2("Vanessa")

#dog.emitir_som()
#cat.emitir_som()
#ps1.reclamcao()
#ps2.reclamcao()

#============================================================================#

#polimorfismo
'''
Polimorfismo permite que métodos com o mesmo nome possam ser implementados de maneiras diferentes en classes distintas

'''

#class Animal:
#    def fazer_som(self):
#        pass #metodo abstrato

#class Cachorro(Animal):
#    def fazer_som(self):
#        print("O cachorro faz Au au!")

#class Gato(Animal):
#    def fazer_som(self):
#        print("O gato faz Miau!")

#animais = [Cachorro(), Gato()]

#for animal in animais:
#    animal.fazer_som()

#--------------------------------------------------------------------------#

#class Automovel:
#    def som(Self):
#        pass

#class Moto(Automovel):
#    def som(Self):
#        print("A moto faz BIH!")

#class Carro(Automovel):
#    def som(Self):
#        print("O carro faz VRUUUMMMMM")

#automoveis = [Moto(), Carro()]

#for veiculo in automoveis:
#    veiculo.som()

#============================================================================#

#Encapsulamento
'''
Fornece convenções e recursos que permitem simular o encapsulamento
'''

#Propriedades(Getters e Setters)
'''
Podemos usar o decorador @property para criar métodos que controlam o acesso a atributos privados, permite adicionar
lógica ao obter ou definir valores
'''

#Exemplo

#class Pessoa:
#    def __init__(self, nome):
#        self.__nome = nome

#    @property #getters
#    def  nome(self):
#        return self.__nome

#    @nome.setter #setters
#    def nome(self, novo_nome):
#        if isinstance(novo_nome, str) and novo_nome.strip():
#            self.__nome = novo_nome
#        else:
#            print("nome inválido.")

#Uso da classe
#pessoa = Pessoa("Alice")
#print(pessoa.nome)
#pessoa.nome = "Bob"
#print(pessoa.nome)
#pessoa.nome = ""

#============================================================================#
#Desafio:

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def exibir_informacoes(self, permitir):
        if isinstance(permitir, str):
            self.__nome = permitir

    @idade.setter
    def exibir_informacoes2(self, permitir2):
        if isinstance(permitir2, int):
            self.__idade = permitir2

pessoa = Pessoa("Alice", 30)

#Tentativa de acessar o atributo privado __nome
print(f"O nome da pessoa {pessoa.nome}, sua idade é {pessoa.idade}")

























