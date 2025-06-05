from pydantic import BaseModel
from database import Base
from sqlalchemy import Column, Integer, String, Boolean

# Item Model
class Item(BaseModel):
    task_name: str
    completed: bool = False
    deadline: str = None

    class Config:
        orm_mode = True


# Table Schema
class TodoList(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    completed = Column(Boolean, default=False)
    deadline = Column(String, index=True)

    def __repr__(self):
        return f"<TodoList(id={self.id}, task_name={self.task_name}, completed={self.completed}, deadline={self.deadline})>"