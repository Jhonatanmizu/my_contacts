from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('update/', views.user_update, name='update'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]
