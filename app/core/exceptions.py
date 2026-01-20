from typing import Any


class AppException(Exception):
    """Custom application exception carrying a structured response.

    Attributes:
        code: business-level error code
        message: human readable message
        data: optional payload
        status_code: HTTP status code to return
    """

    def __init__(self, code: str = "1", message: str = "error", data: Any = None, status_code: int = 400):
        super().__init__(message)
        self.code = str(code)
        self.message = message
        self.data = data
        self.status_code = status_code
