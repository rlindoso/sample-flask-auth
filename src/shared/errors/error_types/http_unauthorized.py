from http import HTTPStatus
from src.shared.errors.interfaces.http_error_interface import HttpErrorInterface


class HttpUnauthorized(HttpErrorInterface):

    def __init__(self, message='No permission -- see authorization schemes') -> None:
        super().__init__(message)
        self.status_code = HTTPStatus.UNAUTHORIZED
        self.name = "Unauthorized"
        self.message = message
