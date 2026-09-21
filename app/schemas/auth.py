from pydantic import BaseModel

class Login(BaseModel):
    email: str
    senha: str

class TokenResponse(BaseModel):
    acess_token: str
    token_type: str