from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

# database class to store user apps (gotify side)
class App(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4(), primary_key=True)
    name: str
    user_id: uuid.UUID
    # project_id: str
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    app_token: str
