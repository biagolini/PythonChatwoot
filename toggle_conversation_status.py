import os
import requests
import json
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configurações
account_id = 123123123 # Your chatwoot acount number
conversation_id = 2 # ID of the conversation 
base_url = f"https://app.chatwoot.com/api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_status"
token = os.getenv("CHATWOOT_TOKEN")
output = "output/toggle_conversation_status.json"

# Headers de autenticação
headers = {
    "Content-Type": "application/json",
    "api_access_token": token
}

def toggle_conversation_status():
    response = requests.post(base_url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        # Salva a resposta no arquivo JSON
        with open(output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print(f"Status da conversa alternado com sucesso e salvo em '{output}'.")
    else:
        print(f"Erro ao alternar o status da conversa. Código de status: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    toggle_conversation_status()
