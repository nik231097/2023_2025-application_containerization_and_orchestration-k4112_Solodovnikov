from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Настройки базы данных (SQLite)
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Определение модели пользователя
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


Base.metadata.create_all(bind=engine)


# FastAPI приложение
app = FastAPI(
    title="User API",
    description="API для управления пользователями",
    version="1.0"
)


# Pydantic модель для запросов
class UserCreate(BaseModel):
    name: str
    email: str


@app.get("/")
def read_root():
    return {"message": "Микросервис работает!"}


@app.post("/users/")
def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user


@app.get("/users/")
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users
