from app.database.session import conectar

class AcessoVisitanteRepository:
    def __init__(self, conectar):
        self.conectar_banco = conectar

    def registrar_acesso(self, id_visitante, id_unidade, autorizado_por):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            INSERT INTO acesso_visitante(id_visitante, id_unidade, autorizado_por)
            VALUES(%s, %s, %s)
            """, (id_visitante, id_unidade, autorizado_por))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return resultado

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao registrar entrada: {erro}')
            return 0

        finally: 
            cursor.close()
            conexao.close()

    def registrar_saida(self, cpf):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            UPDATE acesso_visitante
            SET
                data_saida = CURRENT_TIMESTAMP
            WHERE id_visitante = (SELECT id_visitante FROM visitante WHERE cpf = %s) AND data_saida IS NULL
            """, (cpf,))

            resultado = cursor.rowcount

            if resultado > 0:
                conexao.commit()
                return resultado

            conexao.rollback()
            return resultado

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao registrar saída: {erro}')
            return 0

        finally: 
            cursor.close()
            conexao.close() 

    def buscar_acesso_por_id(self, id_acesso):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM acesso_visitante
            WHERE id_acesso = %s
            """, (id_acesso,))

            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            conexao.rollback()
            print(f'Erro ao buscar acesso pelo ID: {erro}')
            return None

        finally: 
            cursor.close()
            conexao.close() 

    def buscar_acesso_por_autorizado_por(self, autorizado_por):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM acesso_visitante
            WHERE autorizado_por = %s
            """, (autorizado_por,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao buscar acesso pelo morador autorizador: {erro}')
            return []

        finally: 
            cursor.close()
            conexao.close() 

    def listar_acessos(self):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM acesso_visitante
            """)

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao listar acessos: {erro}')
            return []

        finally: 
            cursor.close()
            conexao.close()    

    def listar_acessos_por_visitante(self, id_visitante):     
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM acesso_visitante
            WHERE id_visitante = %s
            """, (id_visitante,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao listar acessos por visitante: {erro}')
            return []

        finally: 
            cursor.close()
            conexao.close()    

    def listar_acessos_por_unidade(self, id_unidade):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM acesso_visitante
            WHERE id_unidade = %s
            """, (id_unidade,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao listar acessos pela unidade: {erro}')
            return []

        finally: 
            cursor.close()
            conexao.close()   

    def listar_acessos_por_condominio(self, id_condominio):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM acesso_visitante
            WHERE id_condominio = %s
            """, (id_condominio,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao listar acessos pelo condomínio: {erro}')
            return []

        finally: 
            cursor.close()
            conexao.close()  

    def listar_visitantes_presentes(self, id_condominio):
        conexao = self.conectar_banco()

        try:
            cursor = conexao.cursor()

            cursor.execute("""
            SELECT * FROM acesso_visitante
            WHERE id_condominio = %s AND data_saida IS
            """, (id_condominio,))

            resultado = cursor.fetchall()

            if not resultado:
                return []

            return resultado

        except Exception as erro:
            print(f'Erro ao listar acessos ativos pelo condomínio: {erro}')
            return []

        finally: 
            cursor.close()
            conexao.close()  
    
acesso_visitante_repository = AcessoVisitanteRepository(conectar)