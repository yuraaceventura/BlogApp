from fastapi import APIRouter
from .views import router as api_v1_router

router = APIRouter(tags=["api_v1"], prefix="/api/v1")
router.include_router(api_v1_router)