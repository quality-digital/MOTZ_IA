from Test_Extracao_Freshdesk import get_last_ticket, get_ticket_details
from Test_Analise_IA import extrair_cpf_nota_fiscal
from Test_Acionamento_RPA import autenticar_rpa, executar_workflow_rpa

def main():
    # 1. Buscar o último ticket
    print("Buscando o último ticket criado no Freshdesk...")
    last_ticket = get_last_ticket()
    if not last_ticket:
        print("Nenhum ticket encontrado.")
        return

    # 2. Buscar detalhes do último ticket
    ticket_id = last_ticket['id']
    print(f"Buscando detalhes do ticket ID={ticket_id}...")
    detailed_ticket = get_ticket_details(ticket_id)
    if not detailed_ticket:
        print("Erro ao obter detalhes do ticket.")
        return

    # 3. Analisar a descrição do ticket para extrair CPF e Nota Fiscal
    descricao = detailed_ticket.get('description', 'Descrição não disponível')
    print("Analisando a descrição do ticket para extrair CPF e Nota Fiscal...")
    cpf, nota_fiscal = extrair_cpf_nota_fiscal(descricao)
    if not cpf or not nota_fiscal:
        print("Erro ao extrair CPF e Nota Fiscal.")
        return

    # 4. Autenticar no RPA
    print("Autenticando no RPA...")
    session_token = autenticar_rpa()
    if not session_token:
        print("Erro na autenticação do RPA.")
        return

    # 5. Executar o workflow do RPA com os dados extraídos
    print("Iniciando o fluxo do RPA com os dados extraídos...")
    response = executar_workflow_rpa(session_token, cpf, nota_fiscal)
    if response:
        print("Fluxo do RPA iniciado com sucesso.")
    else:
        print("Erro ao executar o workflow do RPA.")

if __name__ == "__main__":
    main()
