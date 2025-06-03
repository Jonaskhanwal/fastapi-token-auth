# FastAPI Token Authentication Example

This is a simple FastAPI project demonstrating token-based authentication using OAuth2 password flow with bearer tokens.

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

git clone https://github.com/Jonaskhanwal/fastapi-token-auth.git
cd fastapi-token-auth
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install fastapi uvicorn python-jose

# Running the App
Start the FastAPI server with:
uvicorn main:app --reload
Usage

1. Generate Token

Make a POST request to /token endpoint with form data:
--username: admin
--password: password123

Example with curl:
curl -X POST -F "username=admin" -F "password=password123" http://localhost:8000/token
Successful response:

json
{
  "access_token": "<your_jwt_token_here>",
  "token_type": "bearer"
}


2. Access Protected Endpoint
Use the token to access the /get-student/{student_id} endpoint:
curl -H "Authorization: Bearer <your_jwt_token_here>" http://localhost:8000/get-student/1

Example successful response:

json
{
  "name": "Abhinay",
  "age": 20
}
