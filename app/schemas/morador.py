from pydantic import BaseModel, Field, EmailStr
from datetime import datetime, date

class CriarMorador(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    data_nascimento: date
    cpf: str = Field(min_length=11, max_length=11)
    email: EmailStr
    senha: str

class AtualizarMorador(BaseModel):
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    data_nascimento: date | None = Field(default=None, min_length=3, max_length=100)
    cpf: str | None = Field(default=None, min_length=3, max_length=100)
    email: str | None = Field(default=None, min_length=3, max_length=100)
    data_atualizacao = datetime

class MoradorResponse(BaseModel):
    id_morador: int
    nome: str
    data_nascimento: date
    cpf: str
    email: str
    ativo: bool
    data_criacao: datetime
    data_atualizacao: datetime