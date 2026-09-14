from pydantic import BaseModel, Field
from datetime import datetime
class CriarCondominio(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    cnpj: str = Field(min_length=14, max_length=14)
    endereco: str = Field(min_length=3, max_length=100)

class AtualizarCondominio(BaseModel):
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    endereco: str | None = Field(default=None, min_length=3, max_length=100)

class CondominioResponse(BaseModel):
    id_condominio: int
    nome: str
    cnpj: str
    endereco: str
    ativo: bool
    data_criacao: datetime
    data_atualizacao: datetime | None
