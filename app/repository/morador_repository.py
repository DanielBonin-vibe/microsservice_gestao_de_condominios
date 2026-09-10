from app.database.session import conectar

class MoradorRepository:
    def __init__(self, conectar):
        self.conectar_banco = conectar

    def cadastrar_morador(self, nome, data_nascimento, cpf, email, senha_hash):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO morador(nome, data_nascimento, cpf, email, senha_hash)
            VALUES (%s, %s, %s, %s, %s)
            """, (nome, data_nascimento, cpf, email, senha_hash))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao cadastrar morador: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def buscar_morador_por_id(self, id_morador):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM morador
            WHERE id_morador = %s
            """, (id_morador,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print(f'Não foi possível buscar o morador pelo ID: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def buscar_morador_por_cpf(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM morador
            WHERE cpf = %s
            """, (cpf,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print(f'Não foi possível buscar o morador pelo CPF: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def buscar_morador_por_email(self, email):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM morador
            WHERE email = %s
            """, (email,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print(f'Não foi possível buscar o morador pelo Email: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def listar_moradores(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM morador
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Não foi possível listar os moradores: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def listar_moradores_ativos(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM morador
            WHERE ativo = TRUE
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Não foi possível listar os moradores ativos: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def listar_moradores_por_unidade(self, id_unidade):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM morador
            WHERE id_unidade = %s
            """, (id_unidade,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Não foi possível listar os moradores por unidade: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def atualizar_info_morador(self, nome, data_nascimento, email, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE morador
            SET
                nome = COALESCE(%s, nome),
                data_nascimento = COALESCE(%s, data_nascimento),
                email = COALESCE(%s, email),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE cpf = %s
            """, (nome, data_nascimento, email, cpf))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Não foi possível atualizar o morador em questão: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def atualizar_cpf_morador(self, email, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE morador
            SET
                cpf = COALESCE(%s, cpf),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE email = %s
            """, (cpf, email))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Não foi possível atualizar o CPF do morador em questão: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def atualizar_status_morador(self, cpf, ativo):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE morador
            SET
                ativo = COALESCE(%s, ativo),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE cpf = %s
            """, (ativo, cpf))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Não foi possível atualizar o status do morador em questão: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

morador_repository = MoradorRepository(conectar)