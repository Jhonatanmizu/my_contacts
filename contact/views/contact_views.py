""" Contacts Views """
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    """_summary_
        Contact index view
    """
    contacts = Contact.objects.filter(is_visible=True).order_by("-id")[:10]
    context = {
        'contacts': contacts
    }
    return render(request, 'contact/pages/index.html', context)


def search_contacts(request: HttpRequest) -> HttpResponse:
    """_summary_
        Contact index view
    """
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        return redirect('contact:index')

    contacts = Contact.objects.filter(
        Q(name__icontains=search_term) | Q(email__icontains=search_term),
        is_visible=True
    ).order_by("-id")
    context = {
        'contacts': contacts
    }
    return render(request, 'contact/pages/index.html', context)


def contact(request: HttpRequest, contact_id: int) -> HttpResponse:
    """_summary_
        Contact view
    """
    target_contact = get_object_or_404(Contact, pk=contact_id, is_visible=True)

    context = {
        "document_title": f'{target_contact.name}',
        'contact': target_contact
    }
    return render(request, 'contact/pages/contact.html', context)
