from fastapi import APIRouter, HTTPException, status
from app.service import bloco_service
from app.schemas.bloco import CriarBloco, AtualizarBloco, BlocoResponse

router = APIRouter(
    prefix='/blocos',
    tags=['Blocos']
)

@router.post('/')
def cadastrar_bloco(dados: CriarBloco):
    resultado = bloco_service.cadastrar_bloco(dados.id_condominio, dados.nome)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/condominio/{id_condominio}/bloco/{id_bloco}')
def buscar_bloco_por_id(id_condominio: int, id_bloco: int):
    resultado = bloco_service.buscar_bloco_por_id(id_condominio, id_bloco)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar')
def listar_blocos():
    resultado = bloco_service.listar_blocos()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/condominio/{id_condominio}')
def listar_blocos_por_condominio(id_condominio: int):
    resultado = bloco_service.listar_blocos_por_condominio(id_condominio)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.patch('/atualizar-info/condominio/{id_condominio}/bloco/{id_bloco}')
def atualizar_info_bloco(id_condominio: int, id_bloco: int, dados: AtualizarBloco):
    resultado = bloco_service.atualizar_info_bloco(id_condominio, id_bloco, dados.nome)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.patch('/condominio/{id_condominio}/bloco/{id_bloco}')
def desativar_bloco(id_condominio: int, id_bloco: int):
    resultado = bloco_service.desativar_bloco(id_condominio, id_bloco)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado
