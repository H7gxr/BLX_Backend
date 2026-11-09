from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL de conexão com o banco SQLite
DATABASE_URL = "sqlite:///./banco.db"

# Criar a engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Criar a fábrica de sessões
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe base dos modelos
class Base(DeclarativeBase):
    pass


def criar_db():
    Base.metadata.create_all(bind=engine)

    
# Gerenciar a conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()