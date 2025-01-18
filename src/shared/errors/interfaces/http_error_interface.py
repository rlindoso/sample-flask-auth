from abc import ABC


class HttpErrorInterface(ABC, Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.status_code = 500
        self.name = "Server Error"
        self.message = message