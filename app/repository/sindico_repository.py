from app.database.session import conectar

class SindicoRepository:
    def __init__(self, conectar):
        self.conectar_banco = conectar

    def cadastrar_sindico(self, id_condominio, id_morador, nome, cpf, email):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO sindico(id_morador, nome, cpf, email)
            VALUES(%s, %s, %s, %s, %s)
            """, (id_morador, id_condominio, nome, cpf, email))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao cadastrar síndico: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def buscar_sindico_por_id(self, id_sindico):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM sindico
            WHERE id_sindico = %s
            """, (id_sindico,))

            resultado = cursor.fetchone()
            
            return resultado

        except Exception as erro:
            print(f'Erro ao buscar síndico pelo ID: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def buscar_sindico_por_cpf(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM sindico
            WHERE cpf = %s
            """, (cpf,))

            resultado = cursor.fetchone()
            
            return resultado

        except Exception as erro:
            print(f'Erro ao buscar síndico pelo CPF: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def buscar_sindico_por_email(self, email):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM sindico
            WHERE email = %s
            """, (email,))

            resultado = cursor.fetchone()
            
            return resultado

        except Exception as erro:
            print(f'Erro ao buscar síndico pelo Email: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def listar_sindiscos_por_condominio(self, id_condominio):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM sindico
            WHERE id_condominio = %s
            """, (id_condominio,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado
        
        except Exception as erro:
            print(f'Erro ao buscar síndico por condomínio: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def listar_sindicos(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM sindico
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []
            
            return resultado

        except Exception as erro:
            print(f'Erro ao listar síndicos: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def atualizar_info_sindico(self, cpf, id_condominio, nome, email):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE sindico 
            SET
                id_condominio = COALESCE(%s, id_condominio),
                nome = COALESCE(%s, nome),
                email = COALESCE(%s, email),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE cpf = %s
            """, (id_condominio, nome, email, cpf))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar as informações do síndico: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def atualizar_cpf_sindico(self, email, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE sindico 
            SET
                cpf = %s,
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
            print(f'Erro ao atualizar o CPF do síndico: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def desativar_sindico(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE sindico 
            SET
                ativo =  FALSE,
                data_atualizacao = CURRENT_TIMESTAMP,
                data_fim_mandato = CURRENT_TIMESTAMP
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
            print(f'Erro ao desativar o síndico: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

sindico_repository = SindicoRepository(conectar)