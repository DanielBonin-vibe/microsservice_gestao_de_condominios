from app.repository import funcionario_repository, condominio_repository

class FuncionarioService:
    def __init__(self, funcionario_repository, condominio_repository):
        self.funcionario_repository = funcionario_repository
        self.condominio_repository = condominio_repository

    def cadastrar_funcionario(self, nome, cpf, email, cargo):
        funcionario = self.funcionario_repository.buscar_funcionario_por_cpf(cpf)

        if funcionario is not None:
            return 'Já existe um funcionário cadastrado com o CPF informado.'

        resultado = self.funcionario_repository.cadastrar_funcionario(nome, cpf, email, cargo)

        if resultado == 0:
            return 'Não foi possível cadastrar o funcionário'

        return resultado

    def buscar_funcionario_por_id(self, id_funcionario):
        resultado = self.funcionario_repository.buscar_funcionario_por_id(id_funcionario)

        if resultado is None:
            return 'Funcionário não encontrado.'

        return resultado

    def buscar_funcionario_por_cpf(self, cpf):
        resultado = self.funcionario_repository.buscar_funcionario_por_cpf(cpf)

        if resultado is None:
            return 'Funcionário não encontrado.'

        return resultado
    
    def listar_funcionarios(self):
        resultado = self.funcionario_repository.listar_funcionarios()

        if not resultado:
            return 'Nenhum funcionário foi encontrado.'

        return resultado

    def listar_funcionarios_ativos(self):
        resultado = self.funcionario_repository.listar_funcionarios_ativos()

        if not resultado:
            return 'Nenhum funcionário foi encontrado.'

        return resultado

    def listar_funcionario_por_condominio(self, id_condominio):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar nenhum condomínio vinculado ao ID informado.'
        
        resultado = self.funcionario_repository.listar_funcionarios_por_condominio(id_condominio)

        if not resultado:
            return 'Nenhum funcionário foi encontrado neste condomínio.'

        return resultado

    def listar_funcionarios_ativos_por_condominio(self, id_condominio):
        condominio = self.condominio_repository.buscar_condominio_por_id(id_condominio)

        if condominio is None:
            return 'Não foi possível localizar nenhum condomínio vinculado ao ID informado.'
        
        resultado = self.funcionario_repository.listar_funcionarios_ativos_por_condominio(id_condominio)

        if not resultado:
            return 'Nenhum funcionário ativo foi encontrado neste condomínio.'

        return resultado

    def atualizar_info_funcionario(self, cpf, nome, email, cargo):
        funcionario = self.funcionario_repository.buscar_funcionario_por_cpf(cpf)

        if funcionario is None:
            return 'Não foi possível localizar nenhum funcionário vinculado a este CPF.'

        nome_antigo = funcionario[2]
        email_antigo = funcionario[4]
        cargo_antigo = funcionario[5]

        if ( nome == nome_antigo and email == email_antigo and cargo == cargo_antigo):
            return 'As informações não podem ser iguais'
        
        resultado = self.funcionario_repository.atualizar_info_funcionario(cpf, nome, email, cargo)

        if resultado == 0:
            return 'Não foi possível atualizar as informações do funcionário.'

        return resultado

    def atualizar_cpf_funcionario(self, id_funcionario, cpf):
        funcionario = self.funcionario_repository.buscar_funcionario_por_id(id_funcionario)

        if funcionario is None:
            return 'Não foi localizado nenhum funcionário vinculado ao ID informado.'

    
        resultado = self.funcionario_repository.atualziar_cpf_funcionario(id_funcionario, cpf)

        if resultado == 0:
            return 'Não foi possível atualizar o CPF do funcionário.'

        return resultado

    def atualizar_status_funcionario(self, cpf):
        funcionario = self.funcionario_repository.buscar_funcionario_por_cpf(cpf)

        if funcionario is None:
            return 'Não foi possível localizar nenhum funcionário vinculado a este CPF.'

        resultado = self.funcionario_repository.atualizar_status_funcionario(cpf)

        if resultado == 0:
            return 'Não foi possível atualizar o status do funcionário.'

        return resultado

    def registrar_demissao(self, cpf):
        funcionario = self.funcionario_repository.buscar_funcionario_por_cpf(cpf)

        if funcionario is None:
            return 'Não foi possível localizar nenhum funcionário vinculado a este CPF.'

        resultado = self.funcionario_repository.registrar_demissao(cpf)

        if resultado == 0:
            return 'Não foi possível demitir o funcionário.'

        return resultado
    
funcionario_service = FuncionarioService(funcionario_repository, condominio_repository)