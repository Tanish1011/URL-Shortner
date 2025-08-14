
## **App Code**

### **`app/db/session.py`**
import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()

IN_MEMORY = os.getenv("IN_MEMORY", "false").lower() == "true"
DB_PATH = os.getenv("DB_PATH", "urlshortener.db")

DATABASE_URL = "sqlite:///:memory:" if IN_MEMORY else f"sqlite:///{DB_PATH}"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
