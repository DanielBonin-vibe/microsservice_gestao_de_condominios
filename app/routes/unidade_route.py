from fastapi import APIRouter, HTTPException, status
from app.schemas.unidade import CriarUnidade, AtualizarUnidade, ResponseUnidade
from app.service import unidade_service

router = APIRouter(
    prefix='/unidades',
    tags=['Unidades']
)
@router.post('/')
def cadastrar_unidade(dados: CriarUnidade):
    resultado = unidade_service.cadastrar_unidade(dados.id_bloco, dados.numero, dados.andar, dados.tipo)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-id/{id_unidade}')
def buscar_unidade_por_id(id_unidade: int):
    resultado = unidade_service.buscar_unidade_por_id(id_unidade)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-numero/{id_bloco}, {numero}')
def buscar_unidade_por_numero(id_bloco: int, numero: int):
    resultado = unidade_service.buscar_unidade_por_numero(id_bloco, numero)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar')
def listar_unidades():
    resultado = unidade_service.listar_unidades()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar-por-bloco/{id_bloco}')
def listar_unidades_por_bloco(id_bloco: int):
    resultado = unidade_service.listar_unidades_por_bloco(id_bloco)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.patch('/atualizar-info/{id_unidade}')
def atualizar_info_unidade(id_unidade: int, dados: AtualizarUnidade):
    resultado = unidade_service.atualizar_info_unidade(id_unidade, dados.numero, dados.andar, dados.tipo, dados.ativo)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.patch('/desativar-unidade/{id_unidade}')
def desativar_unidade(id_unidade: int):
    resultado = unidade_service.desativar_unidade(id_unidade)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado