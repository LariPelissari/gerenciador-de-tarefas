from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routes.tarefas import router as tarefas_router

app = FastAPI(
    title="TaskFlow API",
    description="API para gerenciamento de tarefas",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {
        "mensagem": "Bem-vindo à API TaskFlow!"
    }


app.include_router(tarefas_router)
