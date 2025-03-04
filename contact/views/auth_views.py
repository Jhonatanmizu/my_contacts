from django.http import HttpRequest, HttpResponse


def login(request: HttpRequest) -> HttpResponse:
    """
    _summary_
    Contact login view
    Args:
        request (HttpRequest): _description_
    """
    return HttpResponse('Hello world')
