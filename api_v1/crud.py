from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

import database.models
from database.models import Article


async def create_article(session: AsyncSession, title:str, body:str,):
    article = Article(title=title, body=body)
    session.add(article)
    await session.commit()
    return article

async def get_article_by_id(session: AsyncSession, primary_key:int):
    stmt = select(Article).where(Article.id == primary_key)
    article = await session.scalar(stmt)
    return article

async def get_all_articles(session: AsyncSession):
    stmt = select(Article.id, Article.body, Article.title)
    articles = await session.execute(stmt)
    return articles

async def delete_article_by_id(session: AsyncSession, primary_key:int):
    stmt = delete(Article).where(Article.id == primary_key).returning(Article.id)
    deleted_article_id = await session.scalar(stmt)
    await session.commit()
    return deleted_article_id

async def update_article_by_id(session: AsyncSession, primary_key:int, title: str, body:str):
    stmt = update(Article).where(Article.id == primary_key).values(title=title, body=body).returning(Article).where(Article.id == primary_key)
    updated_article = await session.execute(stmt)
    await session.commit()
    return updated_article.scalar()
