from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base

class TarefaCreate(BaseModel):
    titulo: str
    descricao: str | None = None

class TarefaUpdate(BaseModel):
    titulo: str
    descricao: str | None = None

class TarefaStatusUpdate(BaseModel):
    concluida: bool

class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    concluida = Column(Boolean, default=False)