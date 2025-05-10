import os
import json
import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

CHATWOOT_TOKEN = os.getenv("CHATWOOT_TOKEN")
CHATWOOT_BASE_URL = os.getenv("CHATWOOT_BASE_URL", "https://app.chatwoot.com")
output = "output/self_description.json"

def get_profile():
    url = f"{CHATWOOT_BASE_URL}/api/v1/profile"
    headers = {
        "Content-Type": "application/json",
        "api_access_token": CHATWOOT_TOKEN
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Valid token. User data:")
        data = response.json()
        print(data)

        # Save the response to a local JSON file
        with open(output, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Data saved to '{output}'")
    else:
        print(f"Error validating token: {response.status_code} - {response.text}")

if __name__ == "__main__":
    get_profile()
