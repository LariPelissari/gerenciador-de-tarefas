
from pydantic import BaseModel


class TarefaCreate(BaseModel):
    titulo: str
    descricao: str | None = None


class TarefaUpdate(BaseModel):
    titulo: str
    descricao: str | None = None
