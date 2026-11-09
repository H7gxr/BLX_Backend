from src.infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, String, Float, Boolean, Integer

class Produto(Base):
    __tablename__ = 'produto'

    id = Column('id', Integer, primary_key=True, index=True)
    nome = Column('nome', String)
    detalhe = Column('detalhe', String)
    preco = Column('preço', Float)
    disponivel= Column('disponivel', Boolean)


