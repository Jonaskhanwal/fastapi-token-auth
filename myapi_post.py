from fastapi import FastAPI, Depends
from .auth import authenticate_user, verify_token
from .models import TokenResponse

app = FastAPI()

@app.post("/token", response_model=TokenResponse)
def login(token: TokenResponse = Depends(authenticate_user)):
    return token

@app.post("/protected")
def protected_route(user: dict = Depends(verify_token)):
    return {"message": f"Hello, {user['username']}! You have accessed a protected route."}

