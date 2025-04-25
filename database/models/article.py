from datetime import datetime

from sqlalchemy import String, func, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base

class Article(Base):
    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    body: Mapped[str] = mapped_column(Text())
    published_at: Mapped[datetime] = mapped_column(default=datetime.now(),
                                                   server_default=func.now(),)
    updated_at: Mapped[datetime] = mapped_column(server_default=None,
                                                 default=None,
                                                 onupdate=func.now(),
                                                 server_onupdate=func.now(),
                                                 nullable=True,)