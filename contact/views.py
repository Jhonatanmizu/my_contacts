""" Contacts Views """
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.shortcuts import render  # type: ignore

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    """_summary_
    Contact index view
    Args:
        request (HttpRequest): _description_

    Returns:
        HttpResponse: _description_
    """
    return render(request, 'contact/index.html')
