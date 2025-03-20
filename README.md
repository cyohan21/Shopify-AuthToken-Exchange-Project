# Python Auth Token Exchange Project

## Overview 

This project will demonstrate how to acquire auth tokens from shopify stores through exchange of code given by API keys and API secrets.

## Prerequisites

Ensure you have Flask installed. This will all be done locally, so ngrok is not needed.

Before initializing the program, ensure you have replaced the following code:

> SHOPIFY_API_KEY = "INSERT API KEY HERE"  # Replace text with API Key

> SHOPIFY_API_SECRET = "INSERT API SECRET HERE"  # Replace text with API Secret

> SHOP_NAME = "INSERT STORE NAME HERE" # Replace text with Store Name

API key, secret, and store name are all accessible through GitHub secrets. Only collaborators will have access.

## How It Works


When you initialize the program, you will be given a local web server for which you can be authenticated. Enter the following url into your web browser:

> http://localhost:5000/auth

The program will redirect you to Shopify's OAuth authorization page, where the store owner will need to grant the permissions your app needs (read_products, write_products, etc.)

Once the store owner grants permissions, Shopify will automatically bring you to a new page with the code in the URL.

> E.g. http://localhost:5000/auth/callback?code=AUTHORIZATION_CODE&state=123456

The program will then capture said code, and use the code to request an access token via POST. Once the access token exchange has been done, you will then recieve your access token.






