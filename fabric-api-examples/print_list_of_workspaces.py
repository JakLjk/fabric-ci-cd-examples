import requests

from acquire_token import access_token

# 'result' is the MSAL result from acquire_token_interactive()
access_token = access_token()

# Create HTTP client with bearer token
headers = {
    "Authorization": f"Bearer {access_token}"
}

base_url = "https://api.fabric.microsoft.com/v1/"

# Call "list workspaces"
response = requests.get(f"{base_url}workspaces", headers=headers)

print(response.status_code)
print(response.text)
