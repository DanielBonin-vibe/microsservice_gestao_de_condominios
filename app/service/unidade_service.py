from app.repository import unidade_repository, bloco_repository

class UnidadeService:
    def __init__(self, unidade_repository, bloco_repository):
        self.unidade_repository = unidade_repository
        self.bloco_repository = bloco_repository

    def cadastrar_unidade(self, id_bloco, numero, andar, tipo):
        bloco = self.bloco_repository.buscar_bloco_por_id(id_bloco)

        if bloco is None:
            return 'Não foi possível localizar nenhum bloco vinculado ao ID informado.'

        resultado = self.unidade_repository.cadastrar_unidade(id_bloco, numero, andar, tipo)

        if resultado == 0:
            return 'Não foi possível cadastrar unidade.'

        return resultado

    def buscar_unidade_por_id(self, id_unidade):
        resultado = self.unidade_repository.buscar_unidade_por_id(id_unidade)

        if resultado is None:
            return 'Não foi possível localizar a unidade pelo ID'

        return resultado

    def buscar_unidade_por_numero(self, id_bloco, numero):
        bloco = self.bloco_repository.buscar_bloco_por_id(id_bloco)

        if bloco is None:
            return 'Não foi possível localizar o bloco pelo ID.'

        resultado = self.unidade_repository.buscar_unidade_por_numero(id_bloco, numero)

        if resultado is None:
            return 'Não foi possível localizar a unidade pelo numero'

        return resultado

    def listar_unidades(self):
        resultado = self.unidade_repository.listar_unidade()

        if not resultado:
            return 'Não foi possível listar as unidades.'

        return resultado

    def listar_unidades_por_bloco(self, id_bloco):
        bloco = self.bloco_repository.buscar_bloco_por_id(id_bloco)

        if bloco is None:
            return 'Não foi possível listar as unidades por bloco.'

        resultado = self.unidade_repository.listar_unidade(id_bloco)

        if not resultado:
            return 'Não foi possível listar as unidades por bloco.'

        return resultado

    def atualizar_info_unidade(self, id_unidade, numero, andar, tipo, ativo):
        unidade = self.buscar_unidade_por_id(id_unidade)

        if unidade is None:
            return 'Não foi possível localizar a unidade pelo ID.'

        resultado = self.unidade_repository.atualizar_info_unidade(id_unidade, numero, andar, tipo, ativo)

        if resultado == 0:
            return 'Não foi possível atualizar as informações da unidade'

        return resultado
    
    def desativar_unidade(self, id_unidade):
        unidade = self.buscar_unidade_por_id(id_unidade)

        if unidade is None:
            return 'Não foi possível localizar a unidade pelo ID.'

        resultado = self.unidade_repository.desativar_unidade(id_unidade)

        if resultado == 0:
            return 'Não foi possível destaivar a unidade.'

        return resultado
    
unidade_service = UnidadeService(unidade_repository, bloco_repository)