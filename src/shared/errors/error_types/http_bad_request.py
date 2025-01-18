from http import HTTPStatus
from src.shared.errors.interfaces.http_error_interface import HttpErrorInterface


class HttpBadRequestError(HttpErrorInterface):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.status_code = HTTPStatus.BAD_REQUEST
        self.name = "BadRequest"
        self.message = message
