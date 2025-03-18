from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


@login_required(login_url="authentication:signin")
def create(request: HttpRequest) -> HttpResponse:
    """_summary_
        Create Contact view
    """
    form_action = reverse('contact:create')
    form = ContactForm(data=request.POST,
                       files=request.FILES)
    if not request.method == "GET":
        context = {
            "document_title": 'New Contact',
            'form': form,
            "form_action": form_action
        }
        if form.is_valid():
            created_contact = form.save(commit=False)
            created_contact.owner = request.user
            created_contact.save()
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


@login_required(login_url="authentication:signin")
def update(request: HttpRequest, contact_id) -> HttpResponse:
    """_summary_
        Update Contact view
    """
    user = request.user
    contact = get_object_or_404(
        Contact, pk=contact_id, is_visible=True, owner=user.pk)

    form_action = reverse('contact:update', args=(contact_id,))
    form = ContactForm(data=request.POST,
                       files=request.FILES, instance=contact)

    if not request.method == "GET":
        context = {
            "document_title": 'Update Contact',
            'form': form,
            "form_action": form_action
        }
        if form.is_valid():
            created_contact = form.save()
            contact_id = created_contact.pk
            print(f'{created_contact}')
            return redirect('contact:update', contact_id=contact_id)
        return render(request, 'contact/pages/create.html', context)

    new_form = ContactForm(instance=contact)

    context = {
        "document_title": 'Update Contact',
        'form': new_form,
        "form_action": form_action
    }
    return render(request, 'contact/pages/create.html', context)


@login_required(login_url="authentication:signin")
def delete(request: HttpRequest, contact_id) -> HttpResponse:
    """_summary_
        Delete Contact view
    """
    user = request.user
    contact = get_object_or_404(
        Contact, pk=contact_id, is_visible=True, owner=user.pk)
    confirmation = request.POST.get('confirmation', 'no')

    context = {
        "document_title": 'Delete Contact',
        'contact': contact,
        "confirmation": confirmation
    }

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    return render(request, 'contact/pages/contact.html', context=context)
