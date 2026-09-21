import os 
import jwt

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from jwt.exceptions import InvalidTokenError

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def criar_token(dados: dict):    # A função recebe um dicionário
    dados_token = dados.copy()     # Copiamos para não mexermos no arquivo original

    expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    dados_token.update(
        {'exp': expiracao}    # 'exp' é um claim padrão do jwt chamado 'expiration time'
    )

    token = jwt.encode(    # Aqui nos realmente estamos criando o token entregadno 3 parâmetros
        dados_token,
        SECRET_KEY,
        ALGORITHM=ALGORITHM
        )

    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(   # Aqui estamos afzendo o papel inverso do encode (descodificar)
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload    # Paylaod é a parte do JWT que se refere aos dados, ent ele retorna os dados.

    except InvalidTokenError:
        return None