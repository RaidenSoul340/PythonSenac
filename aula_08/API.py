'''
Objetivo:

-Entender o que é API.

-Aprender a consumir dados de uma API com python.

-Utilizar bibliotecas como request e openpyxl.

-Manipular e salvar os dados obtidos em uma arquivo Excel

#----------------------------------------#

-GET: Obtém dados de um servidor.

-POST: Enviar dados para servidor.

-PUT: Atualizar dados no servidor.

-DELETE: Remove dados no servidor.

'''
#==============================================================#

import requests
import openpyxl
'''
#URL da API

url = "https://jsonplaceholder.typicode.com/users"

#Fazendo a requisição GET para a API
response = requests.get(url)

if response.status_code == 200:
    users = response.json()

    #Criando um novo arquivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    #Adicionando os cabeçalhos
    sheet.append(["ID", "Nome", "Email", "Empresa"])

    #Adicionando dados da API ao Excel
    for user in users:
        sheet.append([user['id'], user['name'], user['email'], user['company']['name']])

    #Salvando o arquivo
    workbook.save("Usuarios_api.xlsx")
    print("Dados salvos no arquivo 'usuarios_api.xlsx")

else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")
'''
#--------------------------------------------------------------------#








#==========================================================================#
    #for user in users:
    #    print(f"Nome: {user['name']}, Email: {user['email']}")
    #    print(f"Endereço: {user['address']}, Usuario: {user['username']}")

'''
puxa todos os nomes, email, endereço e usuarios, e mostra na tela
'''
#==========================================================================#
#Verificando o status de requisição
#if response.status_code == 200:
#    users = response.json() #Convertendo a resposta em formato JSON

#    target_name = 'Clementine Bauch' #Recebe o nome da pessoa.

#for user in users:
#        if user['name'] == target_name:
#            print(f"Nome: {user['name']}, Email: {user['email']}")
#            print(f"Endereço: {user['address']}, Usuario: {user['username']}")

'''
Um filtro que ira pegar o nome de 'target_name' e da um print em todas as suas informações 
'''
#==========================================================================#




