""" Contacts Views """
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


@login_required(login_url="authentication:signin")
def index(request: HttpRequest) -> HttpResponse:
    """_summary_
        Contact index view
    """
    user = request.user
    contacts = Contact.objects.filter(
        is_visible=True, owner=user.pk).order_by("-id")

    paginator = Paginator(contacts, 12)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'contact/pages/index.html', context)


@login_required(login_url="authentication:signin")
def search_contacts(request: HttpRequest) -> HttpResponse:
    """_summary_
        Contact index view
    """
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        return redirect('contact:index')
    user = request.user

    contacts = Contact.objects.filter(
        Q(name__icontains=search_term) | Q(email__icontains=search_term),
        is_visible=True, owner=user.pk
    ).order_by("-id")

    paginator = Paginator(contacts, 12)

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'contact/pages/index.html', context)


@login_required(login_url="authentication:signin")
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
