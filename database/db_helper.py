from asyncio import current_task

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session

from config import settings

class DatabaseHelper:
    def __init__(self):
        self.engine = create_async_engine(settings.database.get_url(), echo=False)
        self.session_factory = async_sessionmaker(self.engine, expire_on_commit=False)

    def get_scoped_session(self):
        session = async_scoped_session(self.session_factory, scopefunc=current_task)
        return session

    async def scoped_session_dependency(self):
        session = self.get_scoped_session()
        yield session
        await session.close()

db_helper = DatabaseHelper()