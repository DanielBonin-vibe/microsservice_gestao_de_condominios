from pydantic import BaseModel, Field 
from datetime import datetime

class CriarFuncionario(BaseModel):
    id_condominio: int
    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=11)
    email: str = Field(min_length=3, max_length=100)
    cargo: str = Field(min_length=3, max_length=100)

class AtualizarFuncionario(BaseModel):
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    email: str | None = Field(default=None, min_length=3, max_length=100)
    cargo: str | None = Field(default=None, min_length=3, max_length=100)

class FuncionarioResponse(BaseModel):
    id_condominio: int
    nome: str
    cpf: str
    email: str
    cargo: str
    ativo: bool
    data_admissao: datetime
    data_demissao: datetime | None
    data_criacao: datetime
    data_atualizacao: datetime