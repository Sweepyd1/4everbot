from typing import Final
from fastapi.routing import APIRouter

from .webhook import router as webhook_router

main_router: Final[APIRouter] = APIRouter()
main_router.include_router(webhook_router)
