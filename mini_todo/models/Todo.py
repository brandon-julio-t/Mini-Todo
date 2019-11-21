from Lib import dataclasses

from mini_todo import db


@dataclasses.dataclass
class Todo(db.Model):
    id: int = db.Column(
        db.Integer,
        autoincrement=True,
        index=True,
        primary_key=True,
        unique=True,
        nullable=False)
    todo_content: str = db.Column(db.String, unique=True, nullable=False)
