import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
import json

load_dotenv()

def extrair_cpf_nota_fiscal(descricao):
    # Carregar a chave da API da OpenAI do .env
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("Erro: Chave da API OpenAI não encontrada no arquivo .env")
        return None, None

    # Configurar o modelo OpenAI (usando GPT-4)
    llm = ChatOpenAI(
        model_name="gpt-4",
        openai_api_key=openai_api_key
    )

    # Criação do prompt para extrair CPF e Nota Fiscal
    prompt = f"""
    A seguinte descrição é sobre um ticket de atendimento ao cliente:
    "{descricao}"

    Extraia as seguintes informações:
    - CPF
    - Nota Fiscal

    Responda no seguinte formato JSON:
    {{
        "cpf": "<CPF extraído>",
        "nota_fiscal": "<Nota Fiscal extraída>"
    }}
    """

    try:
        # Utilizando `invoke()` para obter a resposta do LLM
        print("Enviando descrição para análise da IA...")
        resposta = llm.invoke([("system", "Você é um modelo de IA especializado em extrair informações de textos."), ("human", prompt)])
        
        # Verificar se a resposta está no formato JSON e convertê-la em dicionário
        dados = resposta.content.strip()
        try:
            dados_dict = json.loads(dados)
            cpf = dados_dict.get("cpf")
            nota_fiscal = dados_dict.get("nota_fiscal")
            print(f"CPF e Nota Fiscal extraídos: CPF={cpf}, Nota Fiscal={nota_fiscal}")
            return cpf, nota_fiscal
        except json.JSONDecodeError:
            print("Erro: A resposta da IA não está no formato JSON esperado.")
            return None, None

    except Exception as e:
        print(f"Erro ao analisar a descrição com a IA: {e}")
        return None, None
