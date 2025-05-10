import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
account_id = 123123123  # Your Chatwoot account number
attribute_id = 112233  # ID of the previously created attribute
output = "output/custom_attribuite_details.json"
base_url = f"https://app.chatwoot.com/api/v1/accounts/{account_id}/custom_attribute_definitions/{attribute_id}"

# Authentication token
token = os.getenv("CHATWOOT_TOKEN")

# Headers
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "api_access_token": token
}

def get_custom_attribute_details():
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output), exist_ok=True)
        # Save the response to the file
        with open(output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print(f"Attribute details successfully saved to '{output}'.")
    else:
        print(f"Error retrieving attribute details. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    get_custom_attribute_details()
