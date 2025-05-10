import os
import requests
import json
import uuid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
data = {
    "account_id": 123123123 , # Your account ID
    "conversation_id": 2,
    "custom_attributes": {
        "current_conversation": "9e825810-3eb6-4164-9721-f99354dd44dd",
        "previous_conversation": ["3ea0a0e9-2680-47f9-bc22-8e78af10c40d"]
    }
}

output = "output/conversation_update_custom_attributes.json"

# Generate new session ID
new_conversation_id = str(uuid.uuid4())

# Update custom attributes
old_current = data["custom_attributes"].get("current_conversation")
previous = data["custom_attributes"].get("previous_conversation", [])

# Ensure it's a list (in case it's not)
if not isinstance(previous, list):
    previous = []

# Add the previous current_conversation to history
if old_current:
    previous.insert(0, old_current)

# Prepare new custom attributes
custom_attributes_payload = {
    "custom_attributes": {
        "current_conversation": new_conversation_id,
        "previous_conversation": previous
    }
}

# API endpoint and headers
url = f"https://app.chatwoot.com/api/v1/accounts/{data['account_id']}/conversations/{data['conversation_id']}/custom_attributes"
token = os.getenv("CHATWOOT_TOKEN")

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "api_access_token": token
}

def update_conversation_custom_attributes():
    response = requests.post(url, headers=headers, json=custom_attributes_payload)

    if response.status_code == 200:
        result = response.json()
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output), exist_ok=True)
        # Write response to file
        with open(output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print(f"Conversation custom attributes updated successfully and saved to '{output}'.")
    else:
        print(f"Failed to update conversation attributes. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    update_conversation_custom_attributes()
