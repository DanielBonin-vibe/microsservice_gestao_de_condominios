from app.database.session import conectar

class UnidadeRepository:
    def __init__(self, conectar):
        self.conectar_banco = conectar

    def cadastrar_unidade(self, id_bloco, numero, andar, tipo):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO unidade(id_bloco, numero, andar, tipo)
            VALUES(%s, %s, %s, %s)
            """, (id_bloco, numero, andar, tipo))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao cadastrar unidade: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()

    def buscar_unidade_por_id(self, id_unidade):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM unidade
            WHERE id_unidade = %s
            """, (id_unidade,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao buscar unidade pelo ID: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def buscar_unidade_por_numero(self, id_bloco, numero):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM unidade
            WHERE id_bloco = %s AND numero = %s
            """, (id_bloco, numero))

            return cursor.fetchone()

        except Exception as erro:
            print(f'Erro ao buscar unidade pelo número: {erro}')
            return None

        finally:
            cursor.close()
            conexao.close()

    def listar_unidades(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM unidade
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar unidade pelo numero: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close() 

    def listar_unidades_por_bloco(self, id_bloco):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM unidade
            WHERE id_bloco = %s 
            """, (id_bloco,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar unidade pelo numero: {erro}')
            return []

        finally:
            cursor.close()
            conexao.close()         

    def atualizar_info_unidade(self, id_unidade, numero, andar, tipo, ativo):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE unidade
            SET
                numero = COALESCE(%s, numero),
                andar = COALESCE(%s, andar),
                tipo = COALESCE(%s, tipo),
                ativo = COALESCE(%s, ativo),
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE id_numero = %s
            """, (numero, andar, tipo, ativo, id_unidade))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao atualizar as informações da unidade: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()    

    def desativar_undiade(self, id_unidade):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE unidade
            SET
                ativo = FALSE
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE id_unidade = %s
            """, (id_unidade,))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return 0

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao desativar a unidade: {erro}')
            return 0

        finally:
            cursor.close()
            conexao.close()    

unidade_repository = UnidadeRepository(conectar)