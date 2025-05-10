import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
data = {
    "account_id": 123123123 , # Your account ID
    "conversation_id": 2
}

output = "output/conversation_clean_custom_attributes.json"

# Empty custom attributes payload
custom_attributes_payload = {
    "custom_attributes": {}
}

# API endpoint and headers
url = f"https://app.chatwoot.com/api/v1/accounts/{data['account_id']}/conversations/{data['conversation_id']}/custom_attributes"
token = os.getenv("CHATWOOT_TOKEN")

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "api_access_token": token
}

def clear_conversation_custom_attributes():
    response = requests.post(url, headers=headers, json=custom_attributes_payload)

    if response.status_code == 200:
        result = response.json()
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output), exist_ok=True)
        # Write response to file
        with open(output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print(f"Custom attributes cleared and response saved to '{output}'.")
    else:
        print(f"Failed to clear custom attributes. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    clear_conversation_custom_attributes()
