from app.repository import bloco_repository, condominio_repository

class BlocoService:
    def __init__(self, bloco_repository, condominio_repository):
        self.bloco_repository = bloco_repository
        self.condominio_repository = condominio_repository

    def cadastrar_bloco(self, id_condominio, nome):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar o condominio informado.'

        resultado = self.bloco_repository.cadastrar_bloco(id_condominio, nome)

        if resultado == 0:
            return 'Não foi possível cadastrar bloco.'

        return resultado

    def buscar_bloco_por_id(self, id_condominio, id_bloco):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar o condominio informado.'
        

        resultado = self.bloco_repository.buscar_bloco_por_id(id_condominio, id_bloco)

        if resultado is None:
            return 'Não foi possível localizar o bloco pelo ID.'
        
        return resultado

    def listar_blocos(self):
        resultado = self.bloco_repository.listar_blocos()

        if not resultado:
            return 'Não foi possível listar os blocos'

        return resultado

    def listar_blocos_por_condominio(self, id_condominio):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar o condominio informado.'
        

        resultado = self.bloco_repository.listar_blocos_por_condominio(id_condominio)

        if not resultado:
            return 'Não foi possível listar os blocos por condomínio'

        return resultado

    def atualizar_info_bloco(self, id_condominio, id_bloco, nome):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar o condominio informado.'

        bloco = self.bloco_repository.buscar_bloco_por_id(id_bloco)

        if bloco is None:
            return 'Não foi possível localizar o bloco pelo ID.'

        resultado = self.bloco_repository.atualizar_info_bloco(id_condominio, id_bloco, nome)

        if resultado == 0:
            return 'Não foi possível atualizar as informações do bloco.'
        
        return resultado

    def desativar_bloco(self, id_condominio, id_bloco):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar o condomínio informado.'

        bloco = self.bloco_repository.buscar_bloco_por_id(id_bloco)

        if bloco is None:
            return 'Não foi possível localizar o bloco pelo ID.'
        

        resultado = self.bloco_repository.desativar_bloco(id_condominio, id_bloco)

        if resultado == 0:
            return 'Não foi possível desativar o bloco.'
        
        return resultado

        
bloco_service = BlocoService(bloco_repository, condominio_repository)