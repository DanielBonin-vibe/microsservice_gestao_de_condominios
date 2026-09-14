from app.repository import morador_repository

class MoradorService:
    def __init__(self, morador_repository):
        self.morador_repository = morador_repository


    def cadastrar_morador(self, nome, data_nascimento, cpf, email, senha_hash):