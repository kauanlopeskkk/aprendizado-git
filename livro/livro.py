from fastapi import FastAPI, HTTPException

app = FastAPI()

meu_livros = {}

app.get("/livros")

@app.get("/livros")
def get_livros():
    if not meu_livros:
        return {"ERRO": "Não existe nenhum livro cadastrado"}
   
    return {"Livros": [{"id_livros": id_livro, **dados} for id_livro, dados in meu_livros.items()]}
@app.post("/adiciona")
def post_livros(id_livros: int, nome_livros: str, autor_livros: str, ano_livros: int):
    if id_livros in meu_livros:
        raise HTTPException(status_code=400,detail="Esse livro existe.")
    meu_livros[id_livros] = {
        "nome_livros": nome_livros,
        "autor livros": autor_livros,
        "ano_livros": ano_livros
        }
    return {"SUCESSO": "O livro foi criado."}

@app.put("/atualiza/{id_livros}")
def put_livros(id_livros: int, nome_livros: str = None, autor_livros: str = None, ano_livros: int = None):
    Livro = meu_livros.get(id_livros)
    if not Livro:

        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
        if nome_livros:
            Livro["nome_livros"] = nome_livros
        if autor_livros:
            Livro["autor_livros"] = autor_livros
        if ano_livros:
            Livro["ano_livros"] = ano_livros
    meu_livros[id_livros] = Livro
    return {"SUCESSO": "As informações do seu livro foram atualizadas com sucesso"}

@app.delete("/deletar/{id_livros}")
def delete_livros(id_livros: int):
    if id_livros not in meu_livros:
        raise HTTPException(status_code = 404, detail = "Esse livro não foi encontrado")
    del meu_livros[id_livros]
    return {"SUCESSO": "Seu livro foi deletado"}