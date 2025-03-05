
from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_contacts, name='search'),
    path('contact/<int:contact_id>', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.contact, name='update'),
    path('contact/<int:contact_id>/delete/', views.contact, name='delete'),
]
