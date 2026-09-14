from app.repository import acesso_visitante_repository, visitante_repository, morador_repository, unidade_repository,condominio_repository

class AcessoVisitanteService:
    def __init__(self, acesso_visitante_repository, visitante_repository, morador_repository, unidade_repository, condominio_repository):
        self.acesso_visitante_repository = acesso_visitante_repository
        self.visitante_repository = visitante_repository
        self.morador_repository = morador_repository
        self.unidade_repository = unidade_repository
        self.condominio_repository = condominio_repository


    def registrar_acesso(self, id_visitante, id_unidade, autorizado_por):
        morador = self.morador.repository.buscar_morador_por_id(autorizado_por)

        if morador is None:
            return 'Não foi possível localizar o morador que autorizou o acesso.'

        
        unidade = self.unidade_repository.buscar_unidade_por_id(id_unidade)

        if unidade is None:
            return 'Não foi possível localizar a unidade para autorização.'


        visitante = self.visitante_repository.buscar_visitante_por_id(id_visitante)

        if visitante is None:
            return 'O visitante que está tentando acessar o condomínio não está cadastrado.'
        

        resultado = self.acesso_visitante_repository.registrar_acesso(id_visitante, id_unidade, autorizado_por)

        if resultado == 0:
            return 'Não foi possivel registrar o acesso do visitante.'
        
        return resultado

    def registrar_saida(self, cpf):
        visitante = self.visitante_repository.buscar_visitante_por_cpf(cpf)

        if visitante is None:
            return 'O cadastro do visitante não foi localizado.'

        resultado = self.acesso_visitante_repository.registrar_saida(cpf)

        if resultado is None:
            return 'Não foi possível registrar a saída do visitante.'

        return resultado

    def buscar_acesso_por_id(self, id_acesso):
        resultado = self.acesso_visitante_repository.buscar_acesso_por_id(id_acesso)

        if resultado is None:
            return 'Não foi possível buscar o acesso pelo ID de acesso.'

        return resultado

    def buscar_acesso_por_autorizado_por(self, autorizado_por):

        morador = self.morador_repository.buscar_morador_por_id(autorizado_por)

        if morador is None:
            return 'Não foi possível localizar o morador pelo ID.'

        resultado = self.acesso_visitante_repository.buscar_acesso_por_autorizado_por(autorizado_por)

        if resultado is None:
            return 'Não foi possível buscar o acesso por quem autorizou.' 
            
        return resultado

    def listar_acessos(self):
        resultado = self.acesso_visitante_repository.listar_visitantes()

        if not resultado:
            return 'Não há nenhum visitante para listar.'

        return resultado

    def listar_acessos_por_visitante(self, id_visitante):
        visitante = self.visitante_repository.buscar_visitante_por_id(id_visitante)

        if visitante is None:
            return 'Não foi possível localizar o cadatsro do visitante.'

        resultado = self.acesso_visitante_repository.listar_acessos_por_visitante(id_visitante)

        if not resultado:
            return 'Não foi possível listar acessos por visitante.'

        return resultado

    def listar_acessos_por_unidade(self, id_unidade):
        unidade = self.unidade_repository.buscar_unidade_por_id(id_unidade)

        if unidade is None:
            return 'Não foi possível localizar a unidade.'


        resultado = self.acesso_visitante_repository.listar_acessos_por_unidade(id_unidade)

        if not resultado:
            return 'Não foi possível listar nenhum acesso nesta unidade unidade.'

        return resultado

    def listar_acessos_por_condominio(self, id_condominio):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar o condominio informado.'

        resultado = self.acesso_visitante_repository.listar_acessos_por_condominio(id_condominio)

        if not resultado:
            return 'Não há acessos registrados para esse condomínio.'

        return resultado

    def listar_visitantes_presentes(self, id_condominio):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar o condominio informado.'

        resultado  = self.acesso_visitante_repository.listar_visitante_presentes(id_condominio)

        if not resultado:
            return 'Não há acessos registradospresentes neste condomínio.'

        return resultado
        
    
acesso_visitante_service = AcessoVisitanteService(acesso_visitante_repository, visitante_repository, morador_repository, unidade_repository, condominio_repository)