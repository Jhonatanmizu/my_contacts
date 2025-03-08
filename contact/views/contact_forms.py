from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


def create(request: HttpRequest) -> HttpResponse:
    """_summary_
        Create Contact view
    """
    form_action = reverse('contact:create')
    form = ContactForm(data=request.POST)
    if not request.method == "GET":
        context = {
            "document_title": 'New Contact',
            'form': form,
            "form_action": form_action
        }
        if form.is_valid():
            created_contact = form.save()
            contact_id = created_contact.pk
            return redirect('contact:update', contact_id=contact_id)

        return render(request, 'contact/pages/create.html', context)

    new_form = ContactForm()
    context = {
        "document_title": 'New Contact',
        'form': new_form,
        "form_action": form_action
    }
    return render(request, 'contact/pages/create.html', context)


def update(request: HttpRequest, contact_id) -> HttpResponse:
    """_summary_
        Update Contact view
    """
    contact = get_object_or_404(Contact, pk=contact_id, is_visible=True)

    form_action = reverse('contact:update', args=(contact_id,))
    form = ContactForm(data=request.POST, instance=contact)

    if not request.method == "GET":
        context = {
            "document_title": 'New Contact',
            'form': form,
            "form_action": form_action
        }
        if form.is_valid():
            created_contact = form.save()
            contact_id = created_contact.pk
            return redirect('contact:update', contact_id=contact_id)
        return render(request, 'contact/pages/create.html', context)

    new_form = ContactForm(instance=contact)

    context = {
        "document_title": 'New Contact',
        'form': new_form,
        "form_action": form_action
    }
    return render(request, 'contact/pages/create.html', context)
