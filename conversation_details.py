import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
account_id = 123123123  # Your Chatwoot account number
conversation_id = 2
base_url = f"https://app.chatwoot.com/api/v1/accounts/{account_id}/conversations/{conversation_id}"
token = os.getenv("CHATWOOT_TOKEN")
output = "output/conversation_details.json"

# Authentication headers
headers = {
    "Content-Type": "application/json",
    "api_access_token": token
}

def fetch_conversation_details():
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        conversation_details = response.json()
        # Save the response to the JSON file
        with open(output, "w", encoding="utf-8") as f:
            json.dump(conversation_details, f, ensure_ascii=False, indent=4)
        print(f"Conversation details successfully saved to '{output}'.")
    else:
        print(f"Error fetching conversation details. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    fetch_conversation_details()
