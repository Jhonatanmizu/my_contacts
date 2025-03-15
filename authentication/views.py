from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import UserForm


def login(request: HttpRequest) -> HttpResponse:
    """
    _summary_
    User login view
    Args:
        request (HttpRequest): _description_
    """
    return HttpResponse('Hello world')


def register(request: HttpRequest) -> HttpResponse:
    """
    _summary_
    User register view
    """

    form_action = reverse('authentication:register')

    if request.method == 'POST':
        form = UserForm(data=request.POST)
        context = {
            'title': 'Register',
            'form': form,
            "form_action": form_action
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect("contact:index")

    new_form = UserForm()
    context = {
        'title': 'Register',
        'form': new_form,
        "form_action": form_action
    }
    return render(request, 'auth/pages/register.html', context)
