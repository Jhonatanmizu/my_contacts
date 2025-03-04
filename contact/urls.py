
from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('search/', views.search_contacts, name='search'),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
]
