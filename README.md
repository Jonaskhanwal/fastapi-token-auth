# FastAPI Token Authentication Example

This is a simple FastAPI project demonstrating token-based authentication using OAuth2 password flow with bearer tokens.

## Features

- Generate a fake access token by providing username and password.
- Secure endpoint accessible only with a valid token.
- Simple and easy to understand for learning authentication basics.

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

```bash
git clone https://github.com/yourusername/fastapi-token-auth.git
cd fastapi-token-auth
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
