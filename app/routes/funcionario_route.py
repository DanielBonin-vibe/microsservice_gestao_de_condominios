from app.database.session import conectar

class FuncionarioRepository:
    def __init__(self, conectar):
        self.conectar_banco  = conectar

    def cadastrar_funcionario(self, id_condominio, nome, cpf, email, cargo):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO funcionario(id_condominio, nome, cpf, email, cargo)
            VALUES(%s, %s, %s, %s, %s)
            """, (id_condominio, nome, cpf, email, cargo))

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
            conexao.rollback()
            print(f'Erro ao buscar funcionário por ID: {erro}')
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
            conexao.rollback()
            print(f'Erro ao buscar funcionário por CPF: {erro}')
            return None
        
        finally:
            cursor.close()
            conexao.close()

    def buscar_funcionario_por_email(self, email):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM funcionario
            WHERE email = %s
            """, (email,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao buscar funcionário por Email: {erro}')
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
            
            return resultado

        except Exception as erro:
            print(f'Erro ao listar funcionários: {erro}')
            return []
        
        finally:
            cursor.close()
            conexao.close()

    def listar_funcionarios_por_condominio(self, id_condominio):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM funcionario
            WHERE id_condominio = %s
            ORDER BY id_funcionario
            """, (id_condominio,))

            resultado = cursor.fetchall()

            if not resultado:
                return []
            
            return resultado

        except Exception as erro:
            print(f'Erro ao listar funcionários: {erro}')
            return []
        
        finally:
            cursor.close()
            conexao.close()

    def atualizar_info_funcionario(self, cpf, id_condominio, nome, email, cargo):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE funcionario
            SET
                id_condominio = COALESCE(%s, id_condominio),
                nome = COALESCE(%s, nome),
                email = COALESCE(%s, email),
                cargo = COALESCE(%s, cargo),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE cpf = %s
            """, (id_condominio, nome, email, cargo, cpf))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar informações do funcionário: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def atualizar_cpf_funcionario(self, nome, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE funcionario
            SET
                cpf = %s,
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE nome = %s
            """, (cpf, nome))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar informações do CPF funcionário: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def desativar_usuario(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE funcionario
            SET
                ativo = FALSE,
                data_atualizacao = CURRENT_TIMESTAMP,
                data_demissao = CURRENT_TIMESTAMP
            WHERE cpf = %s
            """, (cpf, ))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao destaivar a conta do funcionário: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()   


funcionario_repository = FuncionarioRepository(conectar)