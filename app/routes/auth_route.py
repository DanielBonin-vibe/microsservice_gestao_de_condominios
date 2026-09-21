from fastapi import APIRouter, HTTPException, status
from app.schemas.auth import Login, TokenResponse
from app.service.auth_service import auth_service

router = APIRouter(
    prefix='/auth',
    tags=['Autenticação']
)

@router.post('/login', response_model=TokenResponse)
def login(dados: Login):
    resultado = auth_service.login(dados.email, dados.senha)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=resultado
        )

    return resultado