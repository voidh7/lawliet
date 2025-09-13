import os
import requests
import time
import json
from googlesearch import search

def CEPconsul():
    cep = input("Qual CEP deseja consultar: ")
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Erro status_code {response.status_code}")

def CNPJconsul():
    cnpj = input("Qual CNPJ deseja consultar: ")
    response = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Erro status_code {response.status_code}")

def CPFconsul_google():
    cpf = input("Qual CPF deseja consultar (Google): ")
    query = f"intext:{cpf} typefile:pdf OR ext:txt"
    results = []
    for i in range(0, 30, 10):
        batch = search(query, num_results=10)
        results.extend(batch)
        time.sleep(2)
    for url in results:
        print(url)

def CPFconsul_api():
    cpf = input("Qual CPF deseja consultar via API: ")
    url = f"https://world-ecletix.onrender.com/api/consulta/cpf/{cpf}"
    response = requests.get(url)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Erro status_code {response.status_code}")

def DDDconsul():
    ddd = input("Qual DDD deseja consultar: ")
    response = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}")
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Erro status_code {response.status_code}")

def PlacaConsul():
    placa = input("Qual placa deseja consultar: ")
    url = f"https://world-ecletix.onrender.com/api/consulta/placa/{placa}"
    response = requests.get(url)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Erro status_code {response.status_code}")

def IPconsul():
    ip = input("Qual IP deseja consultar: ")
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Erro status_code {response.status_code}")

def EmailBreach():
    email = input("Qual email deseja consultar: ")
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    elif response.status_code == 404:
        print("Nenhum vazamento encontrado para este email.")
    else:
        print(f"Erro status_code {response.status_code}")

def main():
    os.system("figlet lawliet")
    print("Painel para consultar dados de forma ágil e rápida")
    print("     by vøidh7")

    while True:
        print("\nMenu:")
        print("[1] Consulta CEP")
        print("[2] Consulta CNPJ")
        print("[3] Consulta CPF (Google)")
        print("[4] Consulta CPF (API)")
        print("[5] Consulta DDD")
        print("[6] Consulta Placa de Carro")
        print("[7] Consulta IP")
        print("[8] Consulta Email Vazado")
        print("[0] Sair")

        try:
            typeConsul = int(input("> "))
        except ValueError:
            print("Digite um número válido!")
            continue

        match typeConsul:
            case 1: CEPconsul()
            case 2: CNPJconsul()
            case 3: CPFconsul_google()
            case 4: CPFconsul_api()
            case 5: DDDconsul()
            case 6: PlacaConsul()
            case 7: IPconsul()
            case 8: EmailBreach()
            case 0:
                print("Bye bye")
                time.sleep(1)
                break
            case _:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main() 