# TaskFlow API

API REST para gerenciamento de tarefas, desenvolvida com Python e FastAPI.

O projeto permite criar, listar, consultar, atualizar e excluir tarefas, utilizando SQLite para armazenamento persistente dos dados.

## Tecnologias utilizadas

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- Uvicorn


## Funcionalidades

- Criar uma nova tarefa.
- Listar todas as tarefas cadastradas.
- Buscar uma tarefa pelo ID.
- Atualizar os dados de uma tarefa.
- Excluir uma tarefa.
- Armazenar os dados de forma persistente utilizando SQLite.
- Validar os dados recebidos com Pydantic.
- Tratar erros quando uma tarefa não é encontrada.
- Testar as operações da API com Pytest.


## Endpoints

| Método HTTP | Rota | Descrição |
|---|---|---|
| GET | `/` | Mensagem inicial da API |
| POST | `/tarefas/` | Criar uma tarefa |
| GET | `/tarefas/` | Listar todas as tarefas |
| GET | `/tarefas/{tarefa_id}` | Buscar tarefa pelo ID |
| PUT | `/tarefas/{tarefa_id}` | Atualizar uma tarefa |
| DELETE | `/tarefas/{tarefa_id}` | Excluir uma tarefa |


## Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/LariPelissari/gerenciador-de-tarefas.git
```

### 2. Entrar na pasta do projeto
```bash
cd gerenciador-de-tarefas
```

### 3. Criar um ambiente virtual
```bash
python -m venv backend/.venv
```

### 4. Ativar o ambiente virtual
No Windows PowerShell:
```bash
.\backend\.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 6. Iniciar a API
```bash
cd backend
python -m uvicorn main:app --reload
```

A API estará disponível em:

http://127.0.0.1:8000

### 7. Acessar a documentação interativa
http://127.0.0.1:8000/docs


**Uma observação:** o banco SQLite é criado automaticamente pela aplicação quando ela é iniciada, caso ainda não exista.

## Testes automatizados

O projeto possui testes para validar as operações da API e do repositório.

Para executar todos os testes, utilize:

```bash
python -m pytest -v
```

Atualmente, o projeto possui 17 testes automatizados, todos passando.