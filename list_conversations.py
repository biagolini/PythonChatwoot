import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration variables
account_id = 123123123  # Your Chatwoot account number
base_url = f"https://app.chatwoot.com/api/v1/accounts/{account_id}/conversations"
token = os.getenv("CHATWOOT_TOKEN")
output = "output/list_conversations.json"

# Authentication headers
headers = {
    "Content-Type": "application/json",
    "api_access_token": token
}

def fetch_conversations():
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        conversations = response.json()
        # Save the content to a JSON file
        with open(output, "w", encoding="utf-8") as f:
            json.dump(conversations, f, ensure_ascii=False, indent=4)
        print(f"Conversations successfully saved to '{output}'.")
    else:
        print(f"Error fetching conversations. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    fetch_conversations()
