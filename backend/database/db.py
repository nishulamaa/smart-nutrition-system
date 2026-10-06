from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# =========================
# Database
# =========================

DATABASE_URL = "sqlite:///./nutrition.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


# =========================
# Database Session
# =========================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()