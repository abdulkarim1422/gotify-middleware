from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

# database class to store user data (gotify side)
class User(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4(), primary_key=True)
    username: str
    password: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    client_token: str
    full_name: Optional[str] = None
    last_active: datetime = Field(default=datetime(2022, 10, 5))
