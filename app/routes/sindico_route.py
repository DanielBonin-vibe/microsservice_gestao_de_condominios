from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class CriarSindico(BaseModel):
    id_morador: int
    id_condominio: int    
    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=3, max_length=100)
    email: EmailStr

class AtualizarSindico(BaseModel):
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    cpf: str | None = Field(default=None, min_length=3, max_length=100)
    email: EmailStr | None = None

class ResponseSindico(BaseModel):
    id_sindico: int
    id_morador: int
    id_condominio: int    
    nome: str
    cpf: str
    email: EmailStr
    data_inicio_mandato: datetime
    data_fim_mandato: datetime
    ativo: bool
    data_cricao: datetime
    data_atualizacao: datetime