import requests
import os
from dotenv import load_dotenv

load_dotenv()

def autenticar_rpa():
    url = "https://ondemand.automationedge.com/aeengine/rest/authenticate"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    if not username or not password:
        print("Erro: Usuário ou senha não foram carregados corretamente do arquivo .env")
        return None

    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=data, headers=headers)
    
    if response.status_code == 200:
        session_token = response.json().get('sessionToken')
        if session_token:
            print(f"Autenticado com sucesso. Session Token: {session_token}")
            return session_token
        else:
            print("Autenticação falhou, token não encontrado.")
            return None
    else:
        print(f"Erro na autenticação: {response.status_code} - {response.text}")
        return None

def executar_workflow_rpa(session_token, cpf, nota_fiscal):
    url = "https://ondemand.automationedge.com/aeengine/rest/execute"
    headers = {
        'Content-Type': 'application/json',
        'X-session-token': session_token
    }
    data = {
        "orgCode": "PREMIERIT_QUALITY_PROD",
        "workflowName": "testeIntegracao_IA_RPA",
        "params": [
            {
                "name": "Cpf",
                "value": cpf,
                "type": "String"
            },
            {
                "name": "NotaFiscal",
                "value": nota_fiscal,
                "type": "String"
            }
        ]
    }
    print(f"Executando workflow RPA com CPF={cpf} e Nota Fiscal={nota_fiscal}")
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Workflow executado com sucesso.")
        return response.json()
    else:
        print(f"Erro ao executar workflow: {response.status_code} - {response.text}")
        return None
