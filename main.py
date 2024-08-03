from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from uuid import uuid4

app = FastAPI()

# Настройка базы данных PostgreSQL
DATABASE_URL = "postgresql://test_u5yo_user:eoyqcsNrBojkuiYuSpZHpzwBQu5heeCt@dpg-cqn06j5ds78s7395hkhg-a/test_u5yo"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Post(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True, index=True)
    text = Column(String, index=True)

def init_db():
    Base.metadata.create_all(bind=engine)

init_db()

class PostCreate(BaseModel):
    text: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/posts/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    post_id = str(uuid4())
    db_post = Post(id=post_id, text=post.text)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return {"url": f"/posts/{post_id}"}

@app.get("/posts/{post_id}")
def read_post(post_id: str, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        return {"text": db_post.text}
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Social Network API!"}
    
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

