from http import HTTPStatus
from src.shared.errors.interfaces.http_error_interface import HttpErrorInterface


class HttpNotFoundError(HttpErrorInterface):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.status_code = HTTPStatus.NOT_FOUND
        self.name = "NotFound"
        self.message = message
