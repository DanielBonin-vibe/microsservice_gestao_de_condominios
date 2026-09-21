from app.repository.morador_repository import morador_repository
from app.security.hash import verificar_senha
from app.security.token import criar_token

class AuthService:

    def login(self, email, senha):
        morador = morador_repository.buscar_morador_por_email(email)

        if morador is None:
            return 'E-mail ou senha inválido(s).'

        id_morador = morador[0]
        senha_hash = morador[5]

        if not verificar_senha(senha, senha_hash):
            return 'E-mail ou senha inválido(s).'

        token = criar_token({
            'sub': str(id_morador)
        })

        return {
            'access_token': token,
            'token_type': 'bearer'
        }

auth_service = AuthService()