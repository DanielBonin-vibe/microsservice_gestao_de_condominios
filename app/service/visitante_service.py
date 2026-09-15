from app.repository import visitante_repository

class VisitanteService:
    def __init__(self, visitante_repository):
        self.visitante_repository = visitante_repository

    def cadastrar_visitante(self, nome, cpf, telefone):
        visitante = self.visitante_repository.buscar_visitante_por_cpf(cpf)

        if visitante is not None:
            return 'O CPF informado já está vicnulado a um visitante.'

        resultado = self.visitante_repository.cadastrar_visitante(nome, cpf, telefone)

        if resultado == 0:
            return 'Não foi possível cadastrar o visitante'

        return resultado

    def buscar_visitante_por_cpf(self, cpf):
        resultado = self.visitante_repository.buscar_visitante_por_cpf(cpf)

        if resultado is None:
            return 'Não há nenhum visitante vinculado a este CPF.'

        return resultado
    
    def listar_visitantes(self):
        resultado = self.visitante_repository.listar_visitantes()

        if not resultado:
            return 'Não há nenhum visitante a ser listado.'

        return resultado

    def atualizar_info_visitante(self, cpf, nome, telefone):
        visitante = self.visitante_repository.buscar_visitante_por_cpf(cpf)

        if visitante is None:
            return 'Não foi possível localizar nenhum visitante vinculado ao CPF informado'

        resultado = self.visitante_repository.atualizar_info_visitante(cpf, nome, telefone)

        if resultado == 0:
            return 'Não foi possível atualizar as informações do visitante.'

        return resultado

    def atualizar_cpf_visitante(self, id_visitante, cpf):
        visitante = self.visitante_repository.buscar_visitante_por_id(id_visitante)

        if visitante is None:
            return 'Não foi possível localizar nenhum visitante vinculado ao ID informado.'

        cpf_existente = self.visitante_repository.buscar_visitante_por_cpf(cpf)

        if cpf_existente is not None:
            return 'O CPF informado já está vinculado a outro visitante.'

        resultado = self.visitante_repository.atualizar_cpf_visitante(
            id_visitante,
            cpf
        )

        if resultado == 0:
            return 'Não foi possível atualizar o CPF do visitante.'

        return resultado

    def desativar_visitante(self, cpf):
        visitante = self.visitante_repository.buscar_visitante_por_cpf(cpf)

        if visitante is None:
            return 'Não foi possível localizar nenhum visitante vinculado ao CPF informado'

        resultado = self.visitante_repository.desativar_visitante(cpf)

        if resultado == 0:
            return 'Não foi possível desativar a conta do visitante.'

        return resultado
    
visitante_service = VisitanteService(visitante_repository)