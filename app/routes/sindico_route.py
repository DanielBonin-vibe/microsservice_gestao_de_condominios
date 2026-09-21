from fastapi import APIRouter, HTTPException, status
from pydantic import EmailStr
from app.schemas.sindico import CriarSindico, AtualizarSindico, ResponseSindico
from app.service import sindico_service

router = APIRouter(
    prefix='/sindicos',
    tags=['Síndicos']
)

@router.post('/')
def cadastrar_sindico(dados: CriarSindico):
    resultado = sindico_service.cadastrar_sindico(dados.id_condominio, dados.id_morador, dados.nome, dados.cpf, dados.email)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-id/{id_sindico}')
def buscar_sindico_por_id(id_sindico: int):
    resultado = sindico_service.buscar_sindico_por_id(id_sindico)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-cpf/{cpf}')
def buscar_sindico_por_cpf(cpf: int):
    resultado = sindico_service.buscar_sindico_por_cpf(cpf)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado    

@router.get('/buscar-por-email/{email}')
def buscar_sindico_por_email(email: EmailStr):
    resultado = sindico_service.buscar_sindico_por_email(email)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado  

@router.get('/listar-por-condominio/{id_condominio}')
def listar_sindicos_por_condominio(id_condominio: int):
    resultado = sindico_service.listar_sindicos_por_condominio(id_condominio)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado  

@router.get('/listar')
def listar_sindicos():
    resultado = sindico_service.listar_sindicos()

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado  

@router.patch('/atualizar-info/{cpf}')
def atualizar_info_sindico(cpf: int, dados: AtualizarSindico):
    resultado = sindico_service.atualizar_info_sindico(cpf, dados.id_condominio, dados.nome, dados.email)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado  

@router.patch('/atualizar-cpf/{email}')
def atualizar_cpf_sindico(email: EmailStr, cpf: int):
    resultado = sindico_service.atualizar_cpf_sindico(email, cpf)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado  

@router.patch('/desativar/{cpf}')
def desativar_sindico(cpf: int):
    resultado = sindico_service.desativar_sindico(cpf)

    if isinstance (resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado