from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
DATABASE_URL = "sqlite:///./banco.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()

class Users(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name =  Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String, nullable=False)
    
    def __init__(self, email, senha, name="User"):
        self.email = email
        self.senha = senha
        self.name = name
        