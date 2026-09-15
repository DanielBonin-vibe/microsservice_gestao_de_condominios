from app.repository import sindico_repository, morador_repository, condominio_repository

class SindicoService:
    def __init__(self, sindico_repository, morador_repository, condominio_repository):
        self.sindico_repository = sindico_repository
        self.morador_repository = morador_repository
        self.condominio_repository = condominio_repository

    def cadastrar_sindico(self, id_condominio, id_morador, nome, cpf, email):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar o condomínio com o ID informado.'

        morador = self.morador_repository.buscar_morador_por_id(id_morador)

        if morador is None:
            return 'Não foi possível localizar o morador com o ID informado.'

        resultado = self.sindico_repository.cadastrar_sindico(id_condominio, id_morador, nome, cpf, email)

        if resultado == 0:
            return 'Não foi possível cadastrar o síndico em questão.'

        return resultado

    def buscar_sindico_por_id(self, id_sindico):
        resultado = self.sindico_repository.buscar_sindico_por_id(id_sindico)

        if resultado is None:
            return 'Não foi possível localizar o síndico pelo ID informado.'

        return resultado

    def buscar_sindico_por_cpf(self, cpf):
        resultado = self.sindico_repository.buscar_sindico_por_cpf(cpf)

        if resultado is None:
            return 'Não foi possível localizar o síndico pelo CPF informado.'

        return resultado

    def buscar_sindico_por_email(self, email):
        resultado = self.sindico_repository.buscar_sindico_por_email(email)

        if resultado is None:
            return 'Não foi possível localizar o síndico pelo Email informado.'

        return resultado

    def listar_sindicos_por_condominio(self, id_condominio):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar o condomínio em questão.'

        resultado = self.sindico_repository.listar_sindicos_por_condominio(id_condominio)

        if not resultado:
            return 'Não foi localizado nenhum síndico neste condomínio.'

        return resultado

    def listar_sindicos(self):
        resultado = self.sindico_repository.listar_sindicos()

        if not resultado:
            return 'Não foi localizado nenhum síndico.'

        return resultado

    def atualizar_info_sindico(self, cpf, id_condominio, nome, email):
        morador = self.sindico_repository.buscar_sindico_por_cpf(cpf)

        if morador is None:
            return 'Não foi possivel localizar nenhum síndico vinculado ao CPF informado.'

        resultado = self.sindico_repository.atualizar_info_sindico(cpf, id_condominio, nome, email)

        if resultado == 0:
            return 'Não foi possível atualizar as informações do síndico.'

        return resultado

    def atualizar_cpf_sindico(self, email, cpf):
        morador = self.sindico_repository.buscar_sindico_por_email(email)

        if morador is None:
            return 'Não foi possivel localizar nenhum síndico vinculado ao email informado.'

        resultado = self.sindico_repository.atualizar_cpf_sindico(email, cpf)

        if resultado == 0:
            return 'Não foi possível atualizar o CPF do síndico.'

        return resultado

    def desativar_sindico(self, cpf):
        morador = self.sindico_repository.buscar_sindico_por_cpf(cpf)

        if morador is None:
            return 'Não foi possivel localizar nenhum síndico vinculado ao CPF informado.'

        resultado = self.sindico_repository.desativar_sindico(cpf)

        if resultado == 0:
            return 'Não foi possível desativar o síndico'

        return resultado

sindico_service = SindicoService(sindico_repository, morador_repository, condominio_repository)
