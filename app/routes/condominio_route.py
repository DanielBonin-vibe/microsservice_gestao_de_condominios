from fastapi import APIRouter, HTTPException, status
from app.schemas.condominio import CriarCondominio, AtualizarCondominio, AtualizarCnpjCondominio, CondominioResponse
from app.service import condominio_service

router = APIRouter(
    prefix='condominios',
    tags=['Condomínios']
)

@router.post('/')
def cadastrar_condominio(dados: CriarCondominio):
    resultado = condominio_service.cadastrar_condominio(dados.nome, dados.cnpj, dados.endereco)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-cnpj/{cnpj}')
def buscar_condominio_por_cnpj(cnpj: str):
    resultado = condominio_service.buscar_condominio_por_cnpj(cnpj)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado   

@router.get('/listar')
def listar_condominios():
    resultado = condominio_service.listar_condominios()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado  

@router.get('/listar-ativos') 
def listar_condominios_ativos():
    resultado = condominio_service.listar_condominios_ativos()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado  

@router.patch('atualizar-info/condominio/{cnpj}')
def atualizar_info_condominio(cnpj: str, dados: AtualizarCondominio):
    resultado = condominio_service.atualizar_info_condominio(cnpj, dados.nome, dados.endereco)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado 

@router.patch('/atualizar-cnpj/{endereco}/ativar')
def atualizar_cnpj_condominio(endereco: str, dados: AtualizarCnpjCondominio):
    resultado = condominio_service.atualizar_cnpj_condominio(dados.cnpj, endereco)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado 

@router.patch('/atualizar-status/condominio/{cnpj}')
def atualizar_status_condominio(cnpj: str):
    resultado = condominio_service.atualizar_status_condominio(cnpj)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado  

@router.patch('/desativar-status/condominio/{cnpj}/desativar')
def desativar_condominio(cnpj: str):
    resultado = condominio_service.desativar.condominio(cnpj)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado 