from fastapi import APIRouter, HTTPException, status
from app.schemas.morador import CriarMorador, AtualizarMorador, MoradorResponse
from app.service import morador_service
from pydantic import EmailStr

router = APIRouter(
    prefix='/moradores',
    tags=['Moradores']
)

@router.post('/')
def cadastrar_morador(dados: CriarMorador):
    resultado = morador_service.cadastrar_morador(dados.nome, dados.data_nascimento, dados.cpf, dados.email, dados.senha)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-id/{id_morador}')
def buscar_morador_por_id(id_morador: int):
    resultado = morador_service.buscar_morador_por_id(id_morador)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-cpf/{cpf}')
def buscar_morador_por_cpf(cpf: str): 
    resultado = morador_service.buscar_morador_por_cpf(cpf)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-email/{email}')
def buscar_morador_por_email(email: EmailStr):
    resultado = morador_service.buscar_morador_por_email(email)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar')
def listar_moradores():
    resultado = morador_service.listar_moradores()

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado   

@router.get('/listar-ativos')
def listar_moradores_ativos():
    resultado = morador_service.listar_moradores_ativos()

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado   

@router.get('/listar-por-unidade/{id_unidade}')
def listar_moradores_por_unidade(id_unidade: int):
    resultado = morador_service.listar_moradores_por_unidade(id_unidade)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado 

@router.patch('/atualizar-info/{cpf}')
def atualizar_info_morador(cpf: str, dados: AtualizarMorador):
    resultado = morador_service.atualizar_info_morador(cpf, dados.nome, dados.data_nascimento, dados.email)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.patch('/atualizar-cpf/{email}')
def atualizar_cpf_morador(email: EmailStr, cpf: str):
    resultado = morador_service.atualizar_cpf_morador(email, cpf)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.patch('/atualizar-status/{cpf}')
def atualizar_status_morador(cpf: str, ativo: bool):
    resultado = morador_service.atualizar_status_morador(cpf, ativo)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado