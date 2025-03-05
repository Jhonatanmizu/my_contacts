from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    """ Contact Form """
    class Meta:
        """ Contact Form Meta """
        model = Contact
        fields = (
            'name', 'email', 'phone_number', 'description',
            'category', 'owner', 'picture'
        )
