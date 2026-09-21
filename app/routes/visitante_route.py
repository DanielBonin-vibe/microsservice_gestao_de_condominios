from fastapi import APIRouter, HTTPException, status
from app.schemas.visitante import CriarVisitante, AtualizarVisitante, VisitanteResponse
from app.service import visitante_service

router = APIRouter(
    prefix='/visitantes',
    tags=['Visitantes']
)

@router.post('/')
def cadastrar_visitante(dados: CriarVisitante):
    resultado = visitante_service.cadastrar_visitante(dados.nome, dados.cpf, dados.telefone)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-cpf/{cpf}')
def buscar_visitante_por_cpf(cpf: str):
    resultado = visitante_service.buscar_visitante_por_cpf(cpf)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar')
def listar_visitantes():
    resultado = visitante_service.listar_visitante()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.patch('/atualizar-info/{cpf}')
def atualizar_info_visitante(cpf: str, dados: AtualizarVisitante):
    resultado = visitante_service.atualizar_info_visitante(cpf, dados.nome, dados.telefone)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.patch('/atualizar-cpf/{id_visitante}')
def atualizar_cpf_visitante(id_visitante: int, cpf: str):
    resultado = visitante_service.atualizar_cpf_visitante(id_visitante, cpf)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.patch('/desativar/{cpf}')
def desativar_visitante(cpf: str):
    resultado = visitante_service.desativar_visitante(cpf)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado