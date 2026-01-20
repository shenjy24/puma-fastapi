# Puma FastAPI Template

Minimal FastAPI project demonstrating a global response format and exception handling.

Response structure (JSON):

{
  "code": int,
  "message": string,
  "data": any | null
}

Run locally:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Endpoints:

- GET /api/v1/ping  => returns success structure
- GET /api/v1/error => raises a sample `AppException` and returns structured error
