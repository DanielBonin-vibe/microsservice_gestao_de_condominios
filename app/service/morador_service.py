from app.repository import morador_repository, unidade_repository
from app.security.hash import gerar_hash

class MoradorService:
    def __init__(self, morador_repository, unidade_repository):
        self.morador_repository = morador_repository
        self.unidade_repository = unidade_repository


    def cadastrar_morador(self, nome, data_nascimento, cpf, email, senha):
        cpf = self.morador_repository.buscar_morador_por_cpf(cpf)

        if cpf is not None:
            return 'O CPF informado já está vinculado a um morador.'

        senha_hash = gerar_hash(senha)

        resultado = self.morador_repository.cadastrar_morador(nome, data_nascimento, cpf, email, senha_hash)

        if resultado == 0:
            return 'Não foi possível cadastrar o morador.'

        return resultado

    def buscar_morador_por_id(self, id_morador):
        resultado = morador_repository.buscar_morador_por_id(id_morador)

        if resultado is None:
            return 'Nenhum morador localizado.'

        return resultado

    def buscar_morador_por_cpf(self, cpf): 
        resultado = morador_repository.buscar_morador_por_cpf(cpf)

        if resultado is None:
            return 'Nenhum morador localizado.'

        return resultado

    def buscar_morador_por_email(self, email): 
        resultado = morador_repository.buscar_morador_por_email(email)

        if resultado is None:
            return 'Nenhum morador localizado.'

        return resultado

    def listar_moradores(self):
        resultado = morador_repository.listar_moradores()

        if resultado is None:
            return 'Nenhum morador localizado.'

        return resultado

    def listar_moradores_ativos(self):
        resultado = morador_repository.listar_moradores_ativos()

        if resultado is None:
            return 'Nenhum morador ativo localizado.'

        return resultado

    def listar_moradores_por_unidade(self, id_unidade):
        unidade = self.unidade_repository.buscar_unidade_por_id(id_unidade)

        if unidade is None:
            return 'Não foi localizar a unidade em questão.'

        resultado = morador_repository.listar_moradores_por_unidade(id_unidade)

        if resultado is None:
            return 'Nenhum morador localizado nesta unidade.'

        return resultado

    def atualizar_info_morador(self, nome, data_nascimento, email, cpf):
        ...

    def atualizar_cpf_morador(self, email, cpf):
        ...

    def atualizar_status_morador(self, cpf, ativo):
        ...

morador_service = MoradorService(morador_repository)