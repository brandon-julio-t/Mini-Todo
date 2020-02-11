from dataclasses import dataclass

from mini_todo import db


@dataclass
class Todo(db.Model):
    id: int = db.Column(
        db.Integer,
        autoincrement=True,
        index=True,
        primary_key=True,
        unique=True,
        nullable=False)
    todo_content: str = db.Column(db.String, unique=True, nullable=False)
