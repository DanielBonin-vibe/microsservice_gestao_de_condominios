from fastapi import APIRouter, HTTPException, status
from app.schemas.funcionario import CriarFuncionario, AtualizarFuncionario
from app.service import funcionario_service

router = APIRouter(
    prefix='/funcionario',
    tags=['Funcionário']
)

@router.post('/')
def cadastrar_funcionario(dados: CriarFuncionario):
    resultado = funcionario_service.cadastrar_funcionario(dados.nome, dados.cpf, dados.email, dados.cargo)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-id/{id_funcionario}')
def buscar_funcionario_por_id(id_funcionario: int):
    resultado = funcionario_service.buscar_funcionario_por_id(id_funcionario)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-cpf/{cpf}')
def buscar_funcionario_por_cpf(cpf: str):
    resultado = funcionario_service.buscar_funcionario_por_cpf(cpf)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar')
def listar_funcionarios():
    resultado = funcionario_service.listar_funcionarios()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar-ativos') 
def listar_funcionarios_ativos():
    resultado = funcionario_service.listar_funcionarios_ativos()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar-ativos-por-condominio/{id_condominio}')
def listar_funcionario_por_condominio(id_condominio: int):
    resultado = funcionario_service.listar_funcionario_por_condominio(id_condominio)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado 

@router.get('/listar-funcionarios-ativos-por-condominio/{id_condominio}')
def listar_funcionarios_ativos_por_condominio(id_condominio: int):
    resultado = funcionario_service.listar_funcionarios_ativos_por_condominio(id_condominio)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.patch('/atualizar-info/{cpf}')
def atualizar_info_funcionario(cpf: str, dados: AtualizarFuncionario):
    resultado = funcionario_service.atualizar_info_funcionarios(cpf, dados.nome, dados.email, dados.cargo)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.patch('/atualizar-cpf/{id_funcionario}')
def atualizar_cpf_funcionario(id_funcionario: int, dados: AtualizarFuncionario):
    resultado = funcionario_service.atualizar_cpf_funcionarios(id_funcionario, dados.cpf)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.patch('/atualizar-status/{cpf}')
def atualizar_status_funcionario(cpf: str):
    resultado = funcionario_service.atualizar_status_funcionario(cpf)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.patch('/desativar-funcionario/{cpf}')
def registrar_demissao(cpf: str):
    resultado = funcionario_service.registrar_demissao(cpf)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado
