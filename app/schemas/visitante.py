from pydantic import BaseModel, Field
from datetime import datetime

class CriarVisitante(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=11)
    telefone: str = Field(min_length=10, max_length=15)

class AtualizarVisitante(BaseModel):
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    cpf: str | None =  Field(default=None, min_length=11, max_length=11)
    telefone: str | None = Field(default=None, min_length=10, max_length=15)

class VisitanteResponse(BaseModel):
    id_visitante: int
    nome: str
    cpf: str
    telefone: str
    data_criacao: datetime
    data_atualizacao: datetime