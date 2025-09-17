from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


tarefas = []

class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False

@app.post("/tarefas/")
def adicionar_tarefa(tarefa: Tarefa):
    for t in tarefas:
        if t["nome"] == tarefa.nome:
            raise HTTPException(status_code=400, detail="Tarefa já existe.")
    nova_tarefa = {
        "nome": tarefa.nome,
        "descricao": tarefa.descricao,
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    return {"SUCESSO": "Tarefa adicionada com sucesso."}


@app.get("/tarefas/")
def listar_tarefas():
    return {"tarefas": tarefas}

@app.put("/tarefas/{nome}")
def concluir_tarefa(nome: str):
    for t in tarefas:
        if t["nome"] == nome:
            t["concluida"] = True
            return {"SUCESSO": f"Tarefa '{nome}' marcada como concluída."}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")

@app.delete("/tarefas/{nome}")
def remover_tarefa(nome: str):
    for i, t in enumerate(tarefas):
        if t["nome"] == nome:
            tarefas.pop(i)
            return {"SUCESSO": f"Tarefa '{nome}' removida com sucesso."}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")