from fastapi import FastAPI
from app.routes import auth_route, acesso_visitante_route, bloco_route, condominio_route, funcionario_route, morador_route, sindico_route, unidade_route, visitante_route

app = FastAPI()

app.include_router(auth_route.router)
app.include_router(acesso_visitante_route.router)
app.include_router(bloco_route.router)
app.include_router(condominio_route.router)
app.include_router(funcionario_route.router)
app.include_router(morador_route.router)
app.include_router(sindico_route.router)
app.include_router(unidade_route.router)
app.include_router(visitante_route.router)