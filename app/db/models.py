from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class URLMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(index=True, unique=True, max_length=8)
    original_url: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    clicks: int = Field(default=0)
    last_visited: Optional[datetime] = None
    expires_at: Optional[datetime] = None
