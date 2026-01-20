from fastapi import APIRouter, HTTPException
from fastapi import status
from typing import List

from app.services.item_service import service as item_service
from app.schemas.item_schema import Item
from app.core.exceptions import AppException

router = APIRouter()


@router.get("/ping")
async def ping():
    # return raw payload; middleware will wrap into {code,message,data}
    return {"pong": "pong"}


@router.get("/error")
async def sample_error():
    raise AppException(code="1001", message="Sample business error", status_code=400)


@router.get("/items", response_model=List[Item])
async def list_items():
    return item_service.list_items()


@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = item_service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(payload: Item):
    created = item_service.create_item(payload.dict(exclude={"id"}))
    return created
