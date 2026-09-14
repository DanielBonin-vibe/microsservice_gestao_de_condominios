from datetime import datetime
from pydantic import BaseModel, Field

class CriarBloco(BaseModel):
    id_condominio: int
    nome: str = Field(min_length=3, max_length=100)

class BlocoResponse(BaseModel):
    id_bloco: int
    id_condominio: int
    nome: str
    ativo: bool
    data_criacao: datetime
    data_atualizacao: datetime