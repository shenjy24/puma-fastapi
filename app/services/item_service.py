from typing import Dict, List, Optional
from app.schemas.item_schema import Item


class ItemService:
    def __init__(self):
        self._store: Dict[int, Item] = {}
        self._next = 1

    def list_items(self) -> List[Item]:
        return list(self._store.values())

    def get_item(self, item_id: int) -> Optional[Item]:
        return self._store.get(item_id)

    def create_item(self, payload: dict) -> Item:
        item = Item(id=self._next, **payload)
        self._store[self._next] = item
        self._next += 1
        return item


service = ItemService()

__all__ = ["service", "ItemService"]
