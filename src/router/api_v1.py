from fastapi import APIRouter

from src.example_fastapi_module.router import router as example_router

router = APIRouter(prefix="/v1")
router.include_router(example_router)
