from app.database.session import conectar

class BlocoRepository:
    def __init__(self, conectar):
        self.conectar_banco = conectar

    def cadastrar_bloco(self, id_condominio, nome):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO bloco(id_condominio, nome)
            VALUES(%s, %s)
            """, (id_condominio, nome))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Não foi possível cadastrar o bloco: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def buscar_bloco_por_id(self, id_bloco):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM bloco
            WHERE id_bloco = %s
            """, (id_bloco,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print(f'Não foi possível buscar o bloco por ID: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def listar_blocos(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM bloco
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Não foi possível listar os blocos: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def listar_blocos_por_condominio(self, id_condominio):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM bloco
            WHERE id_condominio = %s
            ORDER BY id_bloco
            """, (id_condominio,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Não foi possível listar os blocos por condomínio: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()

    def atualizar_info_bloco(self, id_condominio, id_bloco, nome):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE bloco
            SET
                nome = COALESCE(%s, nome),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE id_condominio = %s AND id_bloco = %s
            """, (nome, id_condominio, id_bloco))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Não foi possível atualizar as informações do bloco: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def desativar_bloco(self, id_condominio, id_bloco):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE bloco
            SET
                ativo = FALSE,
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE id_condominio = %s AND id_bloco = %s
            """, (id_condominio, id_bloco))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Não foi possível desativar o bloco: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()
  
bloco_repository = BlocoRepository(conectar)

