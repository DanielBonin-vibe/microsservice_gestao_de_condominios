from app.database.session import conectar

class CondominioRepository:
    def __init__(self, conectar):
        self.conectar_banco = conectar


    def cadastrar_condominio(self, nome, cnpj, endereco):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO condominio (nome, cnpj, endereco)
            VALUES (%s, %s, %s)
            """, (nome, cnpj, endereco))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao cadastrar condomínio: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def buscar_condominio_por_id(self, id_condominio):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM condominio
            WHERE id_condominio = %s
            """, (id_condominio,))

            resultado = cursor.fetchone()

            if resultado is None:
                return None

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar condomínio por ID: {erro}')
            return None
        
        finally:
            cursor.close()
            conexao.close()

    def buscar_condominio_por_cnpj(self, cnpj):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM condominio
            WHERE cnpj = %s
            """, (cnpj,))

            resultado = cursor.fetchone()

            if resultado is None:
                return None

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar condomínio por CNPJ: {erro}')
            return None
        
        finally:
            cursor.close()
            conexao.close()

    def listar_condominios(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM condominio
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao listar condomínios: {erro}')
            return []
        
        finally:
            cursor.close()
            conexao.close()

    def listar_condominios(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM condominio
            WHERE ativo = TRUE
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao listar condomínios: {erro}')
            return []
        
        finally:
            cursor.close()
            conexao.close()

    def atualizar_info_condominio(self, cnpj,  nome, endereco):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE condominio
            SET
                nome = COALESCE(%s, nome),
                endereco = COALESCE(%s, endereco),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE cnpj = %s
            """, (nome, endereco, cnpj))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar as informações do condomínio: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def atualizar_cnpj_condominio(self, cnpj, endereco):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE condominio
            SET
                cnpj = COALESCE(%s, cnpj),
                data_atualizacao = CURRENT_TIMESTAMP
            where endereco = %s
            """, (cnpj, endereco))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar as informações do condomínio: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def atualizar_status_condominio(self, ativo, cnpj):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE condominio
            SET
                ativo = COALESCE(%s, ativo),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE cnpj = %s
            """, (ativo, cnpj))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar o status do condomínio: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()

    def desativar_condominio(self, cnpj):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE condominio
            SET
                ativo = FALSE,
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE cnpj = %s
            """, (cnpj,))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao desativar o condomínio: {erro}')
            return 0
        
        finally:
            cursor.close()
            conexao.close()  

condominio_repository = CondominioRepository(conectar)