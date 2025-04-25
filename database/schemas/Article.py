from datetime import datetime

from pydantic import BaseModel

class ArticleSchema(BaseModel):
    id: int
    title: str
    body: str
    published_at: datetime
    updated_at: datetime