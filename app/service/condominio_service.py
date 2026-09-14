from app.repository import condominio_repository

class CondominioService:
    def __init__(self, condominio_repository):
        self.condominio_repository = condominio_repository

    def cadastrar_condominio(self, nome, cnpj, endereco):
        condominio = self.condominio_repository.buscar_condominio_por_cnpj(cnpj)

        if condominio is not None:
            return 'O CNPJ já está cadastrado em um condomínio.'

        resultado = self.condominio_repository.cadastrar_condominio(nome, cnpj, endereco)

        if resultado == 0:
            return 'Não foi possível cadastrar o condomínio.'

        return resultado

    def buscar_condominio_por_cnpj(self, cnpj):
        resultado = self.condominio_repository.buscar_condominio_por_cnpj(cnpj)

        if resultado is None:
            return 'O CNPJ informado não está vinculado a nenhum condomínio.'

        return resultado

    def listar_condominios(self):
        resultado = self.condominio_repository.listar_condominios()

        if not resultado:
            return 'Não há nenhum condomínio para listar.'

        return resultado

    def listar_condominios_ativos(self):
        resultado = self.condominio_repository.listar_condominios_ativos()

        if not resultado:
            return 'Não há nenhum condomínio ativo para listar.'

        return resultado

    def atualizar_info_condominio(self, cnpj,  nome, endereco):
        condominio_por_endereco = self.condominio_repository.buscar_condominio_por_cnpj(cnpj)

        if condominio_por_endereco is None:
            return 'Não foi possível localizar o condomínio informado.'

        resultado = self.condominio_repository.atualizar_info_condominio(cnpj,  nome, endereco)

        if resultado == 0:
            return 'Não foi possível atualizar as informações do condomínio.'

        return resultado

    def atualizar_cnpj_condominio(self, cnpj, endereco):
        endereco = self.condominio_repository.buscar_condominio_por_endereco(endereco)

        if endereco is None:
            return 'Não foi possível localizar o condomínio pelo endereço informado.'

        condominio = self.condominio_repository.buscar_condominio_por_cnpj(cnpj)

        if condominio is not None:
            return 'O CNPJ informado já está cadastrado em outro condomínio.'

        resultado = self.condominio_repository.atualizar_cnpj_condominio(cnpj, endereco)

        if resultado == 0:
            return 'Não foi possível atualizar o CNPJ do condomínio.'
        
        return resultado

    def atualizar_status_condominio(self, ativo, cnpj):
        condominio = self.condominio_repository.buscar_condominio_por_cnpj(cnpj)

        if condominio is None:
            return 'Não foi possível localizar o condomínio informado.'
        
        resultado = self.condominio_repository.atualizar_status_condominio(ativo, cnpj)

        if resultado == 0:
            return 'Não foi possível atualizar o status do condomínio.'
        
        return resultado

    def desativar_condominio(self, cnpj):
        condominio = self.condominio_repository.buscar_condominio_por_cnpj(cnpj)

        if condominio is None:
            return 'Não foi possível localizar o condomínio informado.'

        resultado = self.condominio_repository.desativas_condominio(cnpj)

        if resultado == 0:
            return 'Não foi possível desativar o condomínio.'

        return resultado

condominio_service = CondominioService(condominio_repository)