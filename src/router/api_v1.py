from fastapi import APIRouter

from src.products import router as products_router

router = APIRouter(prefix="/v1")
router.include_router(products_router)
