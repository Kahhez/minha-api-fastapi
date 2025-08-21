import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool = False

class TarefaCreate(BaseModel):
    titulo: str

class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    concluida: Optional[bool] = None


def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            tarefas_json = json.load(arquivo)

            return [Tarefa.model_validate(t) for t in tarefas_json]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_tarefas():
    with open('tarefas.json', 'w') as arquivo:

        tarefas_dict = [t.model_dump() for t in db_tarefas]
        json.dump(tarefas_dict, arquivo, indent=4)


db_tarefas = carregar_tarefas()


@app.get("/")
def read_root():
    return {"message": "API de Tarefas com FastAPI"}

@app.get("/tarefas", response_model=List[Tarefa])
def get_tarefas():
    return db_tarefas

@app.post("/tarefas", response_model=Tarefa, status_code=201)
def add_tarefa(tarefa: TarefaCreate):

    ultimo_id = db_tarefas[-1].id if db_tarefas else 0
    novo_id = ultimo_id + 1
    
    nova_tarefa = Tarefa(id=novo_id, titulo=tarefa.titulo, concluida=False)
    db_tarefas.append(nova_tarefa)
    salvar_tarefas()
    return nova_tarefa

@app.get("/tarefas/{id}", response_model=Tarefa)
def get_tarefa_por_id(id: int):
    for tarefa in db_tarefas:
        if tarefa.id == id:
            return tarefa

    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.put("/tarefas/{id}", response_model=Tarefa)
def update_tarefa(id: int, tarefa_update: TarefaUpdate):
    for tarefa in db_tarefas:
        if tarefa.id == id:

            update_data = tarefa_update.model_dump(exclude_unset=True)
            
            for key, value in update_data.items():
                setattr(tarefa, key, value)
            
            salvar_tarefas()
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/tarefas/{id}")
def delete_tarefa(id: int):
    tarefa_a_deletar = None
    for tarefa in db_tarefas:
        if tarefa.id == id:
            tarefa_a_deletar = tarefa
            break
    
    if tarefa_a_deletar:
        db_tarefas.remove(tarefa_a_deletar)
        salvar_tarefas()
        return {"message": "Tarefa deletada com sucesso"}
    
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
