from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    """ Contact Form """

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Type your name here'
        }),
        help_text='Type the contact name here'
    )

    class Meta:
        """ Contact Form Meta """
        model = Contact
        fields = (
            'name', 'phone_number',
            'email', 'description', 'category',
            'picture',
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
