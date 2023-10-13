# jwt-generator
This repository contains a Python script that demonstrates how to work with JSON Web Tokens (JWT) using the `jwt` library. This script provides a basic example of how to create and use JWTs with Python.

## Getting Started
1. Clone or download this repository to your local machine.

2. Install requirements.txt:
```bash
pip install -r requirements.txt
```
3. Copy `config.py.dist` to `config.py` and set the right config. 

## Run the script using Python
```bash
python jwtGenerator.py
```

This will generate a JWT using the private key and payload data provided in config.py. The JWT will be printed to the console. You can also validate the generated JWT using online tools like jwt.io. Simply paste the JWT into the "Encoded" field to inspect its contents. To make authenticated requests to a service that requires a JWT, you can use the following cURL command. 


## Key Generation
```
openssl genpkey -algorithm RSA -out test.key  
openssl req -x509 -new -key test.key -out test.crt -days 3650
```