"""
Database initialization script
Run this to create the database tables
"""

from database import engine, Base
from models import TodoList  # Import all your models

def init_database():
    """Initialize the database by creating all tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
    print(f"Database file: database.db")

if __name__ == "__main__":
    init_database() 