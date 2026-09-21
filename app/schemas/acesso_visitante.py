from datetime import datetime
from pydantic import BaseModel, Field

class CriarAcessoVisitante(BaseModel):
    id_visitante: int
    id_unidade: int
    autorizado_por: int

class SaidaAcessoVisitante(BaseModel):
    data_saida: datetime | None = None

class RespostaAcessoVisitante(BaseModel):
    id_acesso: int
    id_visitante: int
    id_unidade: int
    autorizado_por: int
    data_entrada: datetime
    data_saida: datetime | None
    status: bool