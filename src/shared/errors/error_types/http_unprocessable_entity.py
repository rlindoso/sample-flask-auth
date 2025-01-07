from src.shared.errors.interfaces.http_error_interface import HttpErrorInterface


class HttpUnprocessableEntityError(HttpErrorInterface):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.status_code = 422
        self.name = "UnprocessableEntity"
        self.message = message
