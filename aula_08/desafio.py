import requests

url = "https://loteriascaixa-api.herokuapp.com/api/federal"

response = requests.get(url)


if response.status_code == 200:
    users = response.json()
    for i, user in enumerate(users):
        if i < 2:
            print(f"Local de Ganhadores: {user['localGanhadores']}")

else:
    print(f"Falha ao obter dados. Status code: {response.status_code}")