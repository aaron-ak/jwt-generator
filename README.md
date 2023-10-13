# jwt-generator
This repository contains a Python script that demonstrates how to work with JSON Web Tokens (JWT) using the `python-jwt` library. JSON Web Tokens are a compact, URL-safe means of representing claims to be transferred between two parties. This script provides a basic example of how to create and use JWTs with Python.

## Getting Started
1. Clone or download this repository to your local machine.

2. Install requirements.txt:
```bash
pip install -r requirements.txt
```
3. Create a `config.py` file in the same directory as the script with the following content:

```python
# config.py

# Path to your private key in PEM format
pathToKey = "path/to/your/private/key.pem"

# Payload data for the JWT
payload_data = {
    "user_id": 123,
    "username": "john_doe"
}

# The service URL where you want to send the JWT
serviceUrl = "https://example.com/api/resource"
```


## Run the script using Python
```bash
python jwtGenerator.py
```

This will generate a JWT using the private key and payload data provided in config.py. The JWT will be printed to the console.

You can also validate the generated JWT using online tools like jwt.io. Simply paste the JWT into the "Encoded" field to inspect its contents.

To make authenticated requests to a service that requires a JWT, you can use the following cURL command:


## Key Generation
```
openssl genpkey -algorithm RSA -out test.key  
openssl req -x509 -new -key test.key -out test.crt -days 3650
```