from app.database.session import conectar

class VisitanteRepository:
    def __init__(self, conectar):
        self.conectar_banco = conectar

    def cadastrar_visitante(self, nome, cpf, telefone):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO visitante(nome, cpf, telefone)
            VALUES(%s, %s, %s)
            """, (nome, cpf, telefone))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao cadastrar visitante: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def buscar_visitante_por_id(self, id_visitante):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM visitante
            WHERE id_visitante = %s
            """, (id_visitante,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar visitante pelo ID: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def buscar_visitante_por_cpf(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM visitante
            WHERE cpf = %s
            """, (cpf,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar visitante pelo CPF: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def listar_visitantes(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM visitante
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []
            
            return resultado

        except Exception as erro:
            print(f'Erro ao listar visitantes: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def atualizar_info_visitante(self, cpf, nome, telefone):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE visitante
            SET
                nome = COALESCE(%s, nome),
                telefone = COALESCE(%s, telefone),
                data_atualizacao = CURRENT_TIMESTAMP           
            WHERE cpf = %s
            """, (nome, telefone, cpf))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar as informações do visitante: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def atualizar_cpf_visitante(self, id_visitante, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE visitante
            SET
                cpf = %s,
                data_atualizacao = CURRENT_TIMESTAMP           
            WHERE id_visitante = %s
            """, (cpf, id_visitante))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar o CPF do visitante: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def desativar_visitante(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE visitante
            SET
                ativo = FALSE,
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
            print(f'Erro ao desativar o cadastro do visitante: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

visitante_repository = VisitanteRepository(conectar)
