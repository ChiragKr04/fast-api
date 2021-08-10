from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URl = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URl, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


# Getting actual database opening/closing
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
