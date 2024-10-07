import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Configurações da API
BASE_URL = "https://usp.freshdesk.com/api/v2"
API_KEY = os.getenv("FRESHDESK_API_KEY")
PASSWORD = os.getenv("FRESHDESK_PASSWORD")

def get_last_ticket():
    """Busca o último ticket criado."""
    url = f"{BASE_URL}/tickets?order_by=created_at&order_type=desc&per_page=1"
    try:
        response = requests.get(url, auth=(API_KEY, PASSWORD))
        response.raise_for_status()
        print("Último ticket buscado com sucesso.")
    except requests.RequestException as e:
        print(f"Erro ao buscar o último ticket: {e}")
        return None

    tickets = response.json()
    if tickets:
        print(f"Último ticket encontrado: {tickets[0]}")
        return tickets[0]
    else:
        print("Nenhum ticket encontrado.")
        return None

def get_ticket_details(ticket_id):
    """Busca os detalhes de um ticket específico pelo ID."""
    ticket_details_url = f"{BASE_URL}/tickets/{ticket_id}"
    try:
        detailed_response = requests.get(ticket_details_url, auth=(API_KEY, PASSWORD))
        detailed_response.raise_for_status()
        print(f"Detalhes do ticket {ticket_id} obtidos com sucesso.")
    except requests.RequestException as e:
        print(f"Erro ao obter detalhes do ticket {ticket_id}: {e}")
        return None

    return detailed_response.json()
