from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# Create engine for connection to the database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create session for database connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base model for database
Base = declarative_base()