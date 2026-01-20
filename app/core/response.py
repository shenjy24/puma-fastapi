from typing import Any, Optional
from pydantic import BaseModel


class ResponseModel(BaseModel):
    code: str
    message: str
    data: Optional[Any] = None


def success(data: Any = None, message: str = "success", code: str = "0") -> dict:
    return ResponseModel(code=str(code), message=message, data=data).dict()


def error(message: str = "error", code: str = "1", data: Any = None) -> dict:
    return ResponseModel(code=str(code), message=message, data=data).dict()
