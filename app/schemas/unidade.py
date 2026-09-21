from pydantic import BaseModel, Field
from datetime import datetime

class CriarUnidade(BaseModel):
    id_condominio: int 
    numero: int
    andar: int
    tipo: str = Field(min_length=3, max_length=100)

class AtualizarUnidade(BaseModel):
    id_condominio: int
    numero: int
    andar: int
    tipo: str | None = Field(default=None, min_length=3, max_length=100)
    data_atualizacao: datetime

class ResponseUnidade(BaseModel):
    id_unidade: int
    id_condominio: int
    numero: int
    andar: int
    tipo: str 
    status: bool
    data_criacao: datetime
    data_atualziacao: datetime