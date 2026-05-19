from datetime import datetime
import uuid

from sqlmodel import Field, Relationship, SQLModel


class Like(SQLModel, table=True):
    __tablename__ = "likes"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id", primary_key=True)
    post_id: uuid.UUID = Field(foreign_key="posts.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: "User" = Relationship(back_populates="likes")
    post: "Post" = Relationship(back_populates="likes")
