""" Contacts Views """
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    """_summary_
    Contact index view
    Args:
        request (HttpRequest): _description_

    Returns:
        HttpResponse: _description_
    """
    return render(request, 'contact/pages/index.html')
