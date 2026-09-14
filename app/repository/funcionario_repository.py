from app.database.session import conectar

class FuncionarioRepository:
    def __init__(self, conectar):
        self.conectar_banco = conectar

    def cadastrar_funcionario(self, nome, cpf, email, cargo):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO funcionario(nome, cpf, email, cargo)
            VALUES(%s, %s, %s, %s)
            """, (nome, cpf, email, cargo))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao cadastrar funcionário: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def buscar_funcionario_por_id(self, id_funcionario):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM funcionario
            WHERE id_funcionario = %s
            """, (id_funcionario,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar funcionário pelo ID: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def buscar_funcionario_por_cpf(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM funcionario
            WHERE cpf = %s
            """, (cpf,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar funcionário pelo CPF: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def listar_funcionarios(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM funcionario
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

        except Exception as erro:
            print(f'Erro ao listar funcionários: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def listar_funcionarios_ativos(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM funcionario
            WHERE status = ATIVO
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao listar funcionários ativos: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def listar_funcionario_por_condominio(self, id_condominio):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM funcionario
            WHERE id_condominio = %s
            """, (id_condominio,))

            resultado = cursor.fetchone()

            if not resultado:
                return []

            return resultado
        
        except Exception as erro:
            print(f'Erro ao listar funcionários por condomínio: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def listar_funcionarios_ativos_por_condominio(self, id_condominio):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM funcionario
            WHERE id_condominio = %s AND status = ATIVO
            """, (id_condominio,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado
        
        except Exception as erro:
            print(f'Erro ao listar funcionários ativos por condomínio: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def atualizar_info_funcionario(self, cpf, nome, email, cargo):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE funcionario
            SET 
                nome = COALESCE(%s, nome),
                email = COALESCE(%s, email),
                cargo = COALESCE(%s, cargo),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE cpf = %s
            """, (nome, email, cargo, cpf))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar as informações do funcionário: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def atualizar_cpf_funcionario(self, id_funcionario, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE funcionario
            SET 
                cpf = COALESCE(%s, cpf),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE id_funcionario = %s
            """, (cpf, id_funcionario))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar o CPF do funcionário: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def atualizar_status_funcionario(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE funcionario
            SET 
                status = ATIVO,
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE cpf = %s
            """, (cpf,))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar o status do funcionário: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def registrar_demissao(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE funcionario
            SET 
                status = INATIVO,
                data_atualizacao = CURRENT_TIMESTAMP,
                data_demissao = CURRENT_TIMESTAMP
            WHERE cpf = %s
            """, (cpf,))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao demitir funcionário: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

funcionar_repository = FuncionarioRepository(conectar)