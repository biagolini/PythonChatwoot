import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
account_id = 123123123  # Your Chatwoot account number
base_url = f"https://app.chatwoot.com/api/v1/accounts/{account_id}/custom_attribute_definitions"
token = os.getenv("CHATWOOT_TOKEN")
output = "output/custom_attribuite_create.json"

# Headers with the specific content type
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "api_access_token": token
}

# Payload for creating the custom attribute
payload = {
    "attribute_display_name": "Section ID",
    "attribute_description": "Unique session identifier for conversation tracking",
    "attribute_key": "section_id",
    "attribute_display_type": 0,  # text
    "attribute_values": [],
    "attribute_model": 0  # conversation
}

def create_custom_attribute():
    response = requests.post(base_url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        # Save the response to the JSON file
        with open(output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print(f"Custom attribute successfully created and saved to '{output}'.")
    else:
        print(f"Error creating custom attribute. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    create_custom_attribute()
