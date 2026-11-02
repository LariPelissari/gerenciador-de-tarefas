from fastapi import FastAPI

from app.routes.tarefas import router as tarefas_router

app = FastAPI(
    title="TaskFlow API",
    description="API para gerenciamento de tarefas",
    version="1.0.0"
)


@app.get("/")
def inicio():
    return {
        "mensagem": "Bem-vindo à API TaskFlow!"
    }


app.include_router(tarefas_router)
