from fastapi import FastAPI, HTTPException

app = FastAPI()

# Banco de dados em memória
meu_jogos = {}

# -------------------------
# GET - Buscar todos os jogos
# -------------------------
@app.get("/jogos")
def get_jogos():
    if not meu_jogos:
        return {"ERRO": "Não existe nenhum jogo cadastrado"}
    return {"Jogos": meu_jogos}

# -------------------------
# POST - Adicionar um novo jogo
# -------------------------
@app.post("/adiciona")
def post_jogos(id_jogos: int, nome_jogos: str, marca_jogos: str, ano_jogos: int):
    if id_jogos in meu_jogos:
        raise HTTPException(status_code=400, detail="Esse jogo já existe.")
    meu_jogos[id_jogos] = {
        "nome_jogos": nome_jogos,
        "marca_jogos": marca_jogos,
        "ano_jogos": ano_jogos
    }
    return {"SUCESSO": "O jogo foi criado."}

# -------------------------
# PUT - Atualizar informações de um jogo
# -------------------------
@app.put("/atualiza/{id_jogos}")
def put_jogos(id_jogos: int, nome_jogos: str = None, marca_jogos: str = None, ano_jogos: int = None):
    jogo = meu_jogos.get(id_jogos)
    if not jogo:
        raise HTTPException(status_code=404, detail="Esse jogo não foi encontrado!")
    else:
        if nome_jogos:
            jogo["nome_jogos"] = nome_jogos
        if marca_jogos:
            jogo["marca_jogos"] = marca_jogos
        if ano_jogos:
            jogo["ano_jogos"] = ano_jogos

    meu_jogos[id_jogos] = jogo
    return {"SUCESSO": "As informações do seu jogo foram atualizadas com sucesso"}

# -------------------------
# DELETE - Deletar um jogo
# -------------------------
@app.delete("/deletar/{id_jogos}")
def delete_jogos(id_jogos: int):
    if id_jogos not in meu_jogos:
        raise HTTPException(status_code=404, detail="Esse jogo não foi encontrado")
    del meu_jogos[id_jogos]
    return {"SUCESSO": "Seu jogo foi deletado"}
