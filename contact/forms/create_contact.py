from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    """ Contact Form """
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Type your name here'
        }),
        help_text='Type the contact name here'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_name(self):
        """ Name must have at least 3 characters """
        name = self.cleaned_data.get('name', '')
        if len(name) < 3:
            self.add_error(
                'name',
                ValidationError(
                    'Name must have at least 3 characters',
                    code='invalid'
                )
            )
        return name

    def clean_phone_number(self):
        """ Phone number must have at least 11 digits """
        phone_number = self.cleaned_data.get('phone_number', '')
        if len(phone_number) < 11:
            self.add_error(
                'phone_number',
                ValidationError(
                    'Phone number must have at least 11 digits',
                    code='invalid'
                )
            )
        return phone_number

    class Meta:
        """ Contact Form Meta """
        model = Contact
        fields = (
            'name', 'email', 'phone_number', 'description',
            'category', 'picture'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Type your name here'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Type your email here'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Type your phone number here',
                "data-mask": "(00) 00000-0000"
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Type your description here'
            }),
        }
