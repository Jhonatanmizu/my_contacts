from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from contact.forms import ContactForm


def create(request: HttpRequest) -> HttpResponse:
    """_summary_
        Create Contact view
    """

    if not request.method == "GET":
        context = {
            "document_title": 'New Contact',
            'form': ContactForm(data=request.POST)
        }
        return render(request, 'contact/pages/create.html', context)

    context = {
        "document_title": 'New Contact',
        'form': ContactForm()
    }
    return render(request, 'contact/pages/create.html', context)
