from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .models import TokenResponse


fake_users_db = {
    "abhinay": {
        "username": "abhinay",
        "password": "sai123",
        "token": "fake-jwt-token-for-abhinay"
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends()) -> TokenResponse:
    user = fake_users_db.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return TokenResponse(access_token=user["token"], token_type="bearer")

def verify_token(token: str = Depends(oauth2_scheme)) -> dict:
    user = next((u for u in fake_users_db.values() if u["token"] == token), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
