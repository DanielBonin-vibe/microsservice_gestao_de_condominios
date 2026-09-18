from fastapi import APIRouter, HTTPException, status
from app.service import acesso_visitante_service
from app.schemas.acesso_visitante import CriarAcessoVisitante, SaidaAcessoVisitante, RespostaAcessoVisitante

router = APIRouter(
    prefix='/acessos-visitantes',
    tags=['Acessos de Visitantes']
)

@router.post('/')
def registrar_acesso(dados: CriarAcessoVisitante):
    resultado = acesso_visitante_service.registrar_acesso(dados.id_visitante, dados.id_unidade, dados.autorizado_por)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return {
        'mensagem': 'Acesso do visitante registrado com sucesso.'
    }


@router.post('/saida')
def registrar_saida(dados: SaidaAcessoVisitante):
    resultado = acesso_visitante_service.registrar_saida(dados.cpf)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return {
            'mensagem': 'Saída do visitante registrado com sucesso.'
        }

@router.get('/buscar-por-id/{id_acesso}')
def buscar_acesso_por_id(id_acesso: int):
    resultado = acesso_visitante_service.buscar_acesso_por_id(id_acesso)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/buscar-por-autorizado-por/{autorizado_por}')
def buscar_acesso_por_autorizado_por(autorizado_por: int):
    resultado = acesso_visitante_service.buscar_acesso_por_autorizado_por(autorizado_por)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar')
def listar_acessos():
    resultado = acesso_visitante_service.listar_acessos()

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=resultado
        )

    return resultado

@router.get('/listar-acessos-por-visitante/{id_visitante}')
def listar_acessos_por_visitante(id_visitante: int):
    resultado = acesso_visitante_service.listar_acessos_por_visitante(id_visitante)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )
    
    return resultado

@router.get('/listar-acessos-por-unidade/{id_unidade}')
def listar_acessos_por_unidade(id_unidade: int):
    resultado = acesso_visitante_service.listar_acessos_por_unidade(id_unidade)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar-acessos-por-condominio/{id_condominio}')
def listar_acessos_por_condominio(id_condominio: int):
    resultado = acesso_visitante_service.listar_acessos_por_condominio(id_condominio)

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado

@router.get('/listar-visitantes-presentes/{id_condominio}')
def listar_visitantes_presentes(id_condominio: int):
    resultado = acesso_visitante_service.listar_visitantes_presentes(id_condominio) 

    if isinstance(resultado, str):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=resultado
        )

    return resultado