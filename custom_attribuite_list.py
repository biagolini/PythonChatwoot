import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
account_id = 123123123 # Your chatwoot acount number
output = "output/custom_attribuite_list.json"
base_url = f"https://app.chatwoot.com/api/v1/accounts/{account_id}/custom_attribute_definitions"

# Authentication token
token = os.getenv("CHATWOOT_TOKEN")

# HTTP headers
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "api_access_token": token
}

def list_custom_attributes():
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output), exist_ok=True)
        # Write response to file
        with open(output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print(f"Custom attributes successfully saved to '{output}'.")
    else:
        print(f"Failed to fetch custom attributes. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    list_custom_attributes()
