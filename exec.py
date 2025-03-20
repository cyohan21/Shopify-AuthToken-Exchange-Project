from flask import Flask, request, redirect
from urllib.parse import quote_plus
import requests

app = Flask(__name__)

SHOPIFY_API_KEY = "INSERT API KEY HERE"  # Replace text with API Key
SHOPIFY_API_SECRET = "INSERT API SECRET HERE"  # Replace text with API Secret
SHOP_NAME = "INSERT STORE NAME HERE" # Replace text with Store Name
REDIRECT_URI = "http://localhost:5000/auth/callback" 

@app.route("/auth")
def auth():

    auth_url = (
        f"https://{SHOP_NAME}.myshopify.com/admin/oauth/authorize?"
        f"client_id={SHOPIFY_API_KEY}&"
        f"scope=read_products,write_products&"
        f"redirect_uri={quote_plus(REDIRECT_URI)}&"
        f"state=123456"
    )
    return redirect(auth_url)

@app.route("/auth/callback")
def auth_callback():
    code = request.args.get("code")
    if not code:
        return "Authorization failed: No code received", 400

    token_url = f"https://{SHOP_NAME}.myshopify.com/admin/oauth/access_token"
    payload = {
        "client_id": SHOPIFY_API_KEY,
        "client_secret": SHOPIFY_API_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(token_url, json=payload)

    print("Shopify Response:", response.status_code, response.text) 

    if response.status_code == 200:
        access_token = response.json().get("access_token")
        return f"Access Token: {access_token}"
    else:
        return f"Error: {response.text}", response.status_code

if __name__ == "__main__":
    app.run(port=5000, debug=True)