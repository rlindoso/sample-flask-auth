from src.shared.infra.http.http_types.http_response import HttpResponse
from src.shared.errors.interfaces.http_error_interface import HttpErrorInterface

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpErrorInterface)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
