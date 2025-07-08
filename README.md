# FastAPI_password_generator

The service provide RESTful API for password generation and strength evaluation.

## Features
- Password generation with parameters
- Password strength evaluation based on entropy
- Input parameters validation
- RESTful interface

## Getting started

1. Clone repository:
```sh
git clone https://github.com/nilondes/FastAPI_password_generator.git
cd FastAPI_password_generator
```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Run server:

```sh
python main.py
```

The service will be available by http://localhost:8000

The SWAGGER is available by http://localhost:8000/docs#

## Endpoints

1. Password generation

GET /api/v1/generator

Supports parameters: length (8-100), use_lowercase, use_uppercase, use_digits, use_special

Example:

GET /api/v1/generator?length=12&use_special=true&use_digits=true

2. Check password strength

GET /api/v1/generator/check

Expects 1 parameter: password

Example:

GET /api/v1/generator/check?password=MyP@ssw0rd!

The strength algorithm is based on formula:

entropy = L * log2(N)

where L is password length and N is sum of length of chosen character sets

Import the provided postman collection file to test endpoints.

The variables are:

{ "base_url": "http://localhost:8000"}.