from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import UpdateUserForm, UserForm


def signin(request: HttpRequest) -> HttpResponse:
    """
    SignIn view
    """
    auth_form = AuthenticationForm(request)
    context = {
        'title': 'Signin',
        'form': auth_form
    }

    if request.method == 'POST':
        auth_form = AuthenticationForm(request, data=request.POST)
        if auth_form.is_valid():
            user = auth_form.get_user()
            context = {
                'title': 'Signin',
                'form': auth_form,
                'user': user
            }
            messages.success(request, "Signin successfully")
            auth.login(request, user)
            return redirect("contact:index")
        messages.error(request, "Invalid credentials")
    return render(request, 'auth/pages/signIn.html', context)


def register(request: HttpRequest) -> HttpResponse:
    """
    Register view
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
        else:
            messages.error(request, "Invalid credentials")

    new_form = UserForm()
    context = {
        'title': 'Register',
        'form': new_form,
        "form_action": form_action
    }
    return render(request, 'auth/pages/register.html', context)


@login_required(login_url="authentication:signin")
def signout(request: HttpRequest) -> HttpResponse:
    """
    SignOut view 
    """
    auth.logout(request)
    return redirect("authentication:signin")


@login_required(login_url="authentication:signin")
def user_update(request: HttpRequest) -> HttpResponse:
    """
    Update view 
    """

    if request.method != "POST":
        create_form = UpdateUserForm(instance=request.user)
        context = {
            "form": create_form
        }
        return render(request, "auth/pages/register.html", context)
    update_form = UpdateUserForm(instance=request.user, data=request.POST)

    if not update_form.is_valid():
        context = {
            "form": update_form
        }
        return render(request, "auth/pages/register.html")
    update_form.save()
    return redirect("authentication:update")
