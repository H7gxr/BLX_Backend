from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def listar_produtos(self):
        produtos = self.db.query(models.Produto).all()
        return produtos


    def criar_produto(self, produto: schemas.Produto):
        produto_criado = models.Produto(nome = produto.nome,
                                        detalhe = produto.detalhe,
                                        preco = produto.preco,
                                        disponivel = produto.disponivel)
        self.db.add(produto_criado)
        self.db.commit()
        self.db.refresh(produto_criado)
        return produto_criado

    



       