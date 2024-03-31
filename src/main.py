import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.bot import bot, dp
from src.core import settings
from src.router.api_v1 import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(dp.start_polling(bot))
    yield


app = FastAPI(
    title=settings.project_name,
    version=settings.project_version,
    lifespan=lifespan,
)

app.include_router(router)
