from pydantic import BaseModel, Field
from datetime import datetime

class CriarUnidade(BaseModel):
    id_bloco: int
    numero: int
    andar: int
    tipo: str = Field(min_length=3, max_length=100)

class AtualizarUnidade(BaseModel):
    numero: int
    andar: int
    tipo: str  | None = Field(default=None, min_length=3, max_length=100)
    data_atualziacao = datetime

class Undiaderesponse(BaseModel):
    id_unidade: int
    id_bloco: int
    numero: int
    andar: int
    tipo: str 
    data_atualziacao = datetime
    ativo: bool
    data_criacao: datetime
    data_atualizaca: datetime