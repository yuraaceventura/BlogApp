import asyncio
from typing import List

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter

from api_v1.crud import create_article, get_article_by_id, get_all_articles, delete_article_by_id, update_article_by_id
from database.db_helper import db_helper
from database.models import Article
from database.schemas.Article import ArticleSchema

router = APIRouter(tags=["api_v1"])

@router.get("/articles")
async def get_articles_endpoint(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return_articles = {}
    articles: list[ArticleSchema] = await get_all_articles(session)
    for article in articles:
        return_articles[article.id] = {
            "id": article.id,
            "title": article.title,
            "body": article.body,
        }
    return return_articles

@router.get("/articles/{primary_key}")
async def get_article_endpoint(primary_key:int ,session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    article: ArticleSchema = await get_article_by_id(session, primary_key)
    return article

@router.delete("/articles/{primary_key}")
async def delete_article_endpoint(primary_key: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    article: ArticleSchema = await delete_article_by_id(session, primary_key)
    return article

@router.post("/articles")
async def create_article_endpoint(title:str, body: str, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    article: ArticleSchema = await create_article(session, title, body)
    return article

@router.put("/articles/{primary_key}")
async def update_article_endpoint(primary_key:int, body:str, title:str, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    article = await update_article_by_id(session, primary_key, title, body)
    return article
