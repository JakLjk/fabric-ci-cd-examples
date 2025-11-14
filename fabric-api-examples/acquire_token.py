# The script’s purpose is to obtain an OAuth 2.0 access token for the Microsoft Fabric REST APIs using interactive authentication.
# Concise breakdown:
# Registers a public client application using your Azure AD app’s Client ID.
# Opens the browser for user sign-in (interactive login).
# Requests the permissions (scopes):
# Workspace.ReadWrite.All
# Item.ReadWrite.All
# Azure AD authenticates the user and returns an access token.
# The script prints the access token.
# You then use that token in HTTP calls to Fabric REST APIs:


from msal import PublicClientApplication

# -------- Parameters --------
CLIENT_ID = "cd012c5f-a2b2-4491-a5c0-e7401fa7fb37"
AUTHORITY = "https://login.microsoftonline.com/organizations"
REDIRECT_URI = "http://localhost"

# Scopes for Fabric APIs
SCOPES = [
    "https://api.fabric.microsoft.com/Workspace.ReadWrite.All",
    "https://api.fabric.microsoft.com/Item.ReadWrite.All"
]

# -------- Acquire token --------
def access_token():
    app = PublicClientApplication(
        client_id=CLIENT_ID,
        authority=AUTHORITY
    )

    result = app.acquire_token_interactive(
        scopes=SCOPES,
        # redirect_uri=REDIRECT_URI
    )

    return result["access_token"]
