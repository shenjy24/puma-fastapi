import json
from typing import Any
from fastapi import Request
from fastapi.responses import JSONResponse, Response


async def response_middleware(request: Request, call_next):
    resp = await call_next(request)

    # read body from response iterator
    body = b""
    async for chunk in resp.body_iterator:
        body += chunk

    # if no body, return standard wrapper
    if not body:
        content = {"code": "0", "message": "success", "data": None}
        return JSONResponse(status_code=resp.status_code, content=content)

    try:
        parsed = json.loads(body.decode())
    except Exception:
        # non-json body, forward as raw string under data
        content = {"code": "0", "message": "success", "data": body.decode(errors="ignore")}
        return JSONResponse(status_code=resp.status_code, content=content)

    # If already wrapped (has code and message), don't double-wrap
    if isinstance(parsed, dict) and "code" in parsed and "message" in parsed:
        return JSONResponse(status_code=resp.status_code, content=parsed)

    content = {"code": "0", "message": "success", "data": parsed}
    return JSONResponse(status_code=resp.status_code, content=content)
