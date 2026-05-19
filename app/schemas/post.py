from datetime import datetime
from typing import List
import uuid

from sqlmodel import SQLModel

from app.schemas.comment import CommentRead
from app.schemas.like import LikeRead


class PostCreate(SQLModel):
    description: str
    user_id: uuid.UUID


class PostRead(SQLModel):
    id: uuid.UUID
    user_id: uuid.UUID
    description: str
    created_at: datetime
    likes_count: int = 0
    comments_count: int = 0


class PostReadDetails(SQLModel):
    id: uuid.UUID
    user_id: uuid.UUID
    description: str
    created_at: datetime
    likes: List[LikeRead] = []
    comments: List[CommentRead] = []
