import os
import requests
import time
import json
import time
from googlesearch import search


def CEPconsul():
    cep = input("qual cep deseja consultar:")
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data,indent=4,ensure_ascii=False))
    else:
        print(f"erro status_code {response.status_code}")


def CNPJconsul():
    cnpj = input("qual o cnpj que deseja consultar:")
    response = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data,indent=4,ensure_ascii=False))
    else:
        print(f"erro status_code {requests.status_code}")




def CPFconsul():
    cpf = input("qual o cpf que deseja consultar:")
    print("""
Eu estou procurando na web vazamentos que contém o cpf,se não retornar nada e por causa da dorking lixo que meu criador colocou nessa beta

Obrigado pela atenção
    """)
    query = f"intext:{cpf} typefile:pdf OR ext:txt"
    results = []
    for i  in range(0,300,10):
        batch = search(query,num_results=10)
        results.extend(batch)

        time.sleep(5)

    for url in results:
        print(url)



def DDDconsul():
    ddd = input("qual o ddd que deseja consulta:")
    response = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd} ")
    data = response.json()

    if response.status_code == 200:
        print(json.dumps(data,indent=4,ensure_ascii=False))
    else:
        print(f"erro status_code {response.status_code}")






os.system("figlet lawliet")
print("painel para consultar dados de forma agil e rapida")
print("     by vøidh7")

print("\n menu")
print("[1]consulta cep")
print("[2]consulta cnpj")
print("[3]consulta cpf")
print("[4]consulta ddd")
print("[0]sair")


typeConsul = int(input("> "))

match typeConsul:
    case 1:
        CEPconsul()

    case 2:
        CNPJconsul()

    case 3:
        CPFconsul()
    case 4:
        DDDconsul()
    case 0:
        print("bye byte")
        time.sleep(1)
        exit()
