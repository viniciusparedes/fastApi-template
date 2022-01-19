from fastapi import FastAPI
from settings.db import connectDb

from models import Pessoa

app = FastAPI()
db = connectDb()


@app.post('/cadastro')
def cadastro(nome: str, usuario: str, senha: str):
    if len(db.query(Pessoa).filter_by(usuario=usuario, senha=senha).all()) == 0:
        x = Pessoa(nome=nome, usuario=usuario, senha=senha)
        db.add(x)
        db.commit()
        return {'status': 'sucesso'}
    else:
        return {'status': 'Usuário já cadastrado'}

