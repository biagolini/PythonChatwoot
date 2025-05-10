import os
import requests
import json
import uuid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fixed configuration
account_id = 123123123  # Your Chatwoot account number
attribute_id = 112233  # ID of the previously created attribute
conversation_id = 2

# Generate a unique session ID
custom_session_id = f"{conversation_id}-{uuid.uuid4()}"

# Output file path
output = "output/custom_attribuite_patch.json"

# Attribute update endpoint
base_url = f"https://app.chatwoot.com/api/v1/accounts/{account_id}/custom_attribute_definitions/{attribute_id}"

# Authentication token
token = os.getenv("CHATWOOT_TOKEN")

# Headers
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "api_access_token": token
}

# Update payload
payload = {
    "attribute_display_name": "Section ID",
    "attribute_description": "Unique session identifier for conversation tracking",
    "attribute_key": "section_id",
    "attribute_display_type": 0,  # text
    "attribute_values": [custom_session_id],
    "attribute_model": 0  # conversation
}

def update_custom_attribute():
    response = requests.patch(base_url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output), exist_ok=True)
        # Save response to the defined path
        with open(output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print(f"Attribute updated with Section ID '{custom_session_id}' and saved to '{output}'.")
    else:
        print(f"Error updating attribute. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    update_custom_attribute()
