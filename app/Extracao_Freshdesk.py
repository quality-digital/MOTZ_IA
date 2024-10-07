import requests
import json


# Configurações da API
BASE_URL = "https://usp.freshdesk.com/api/v2"
API_KEY = "tLr4pb0NTmbkfVx0i73"
PASSWORD = "Misc8871@"


def get_last_ticket():
    """Busca o último ticket criado."""
    url = f"{BASE_URL}/tickets?order_by=created_at&order_type=desc&per_page=1"
    try:
        response = requests.get(url, auth=(API_KEY, PASSWORD))
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao buscar o último ticket: {e}")
        return None

    tickets = response.json()
    if tickets:
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
    except requests.RequestException as e:
        print(f"Erro ao obter detalhes do ticket {ticket_id}: {e}")
        return None

    return detailed_response.json()


def print_ticket_details(ticket):
    """Imprime os detalhes do ticket."""
    if ticket:
        ticket_id = ticket['id']
        print(f"ID: {ticket_id}")
        print(f"Assunto: {ticket['subject']}")
        print(f"Descrição: {ticket.get('description', 'Descrição não disponível')}")
        print("-" * 50)
    else:
        print("Ticket não disponível")


def main():
    # Buscar o último ticket
    last_ticket = get_last_ticket()
    if last_ticket:
        # Buscar detalhes do último ticket
        detailed_ticket = get_ticket_details(last_ticket['id'])
        # Imprimir os detalhes do ticket
        print_ticket_details(detailed_ticket)


if __name__ == "__main__":
    main()
