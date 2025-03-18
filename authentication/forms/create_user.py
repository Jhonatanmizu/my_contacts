from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.forms import ValidationError


class UserForm(forms.ModelForm):
    """ 
        User Form 
    """

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Type your password here'
    }),)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Type your password confirmation here'
    }), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type your first name here',
    }), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type your last name here'
    }), required=True)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Type your email here'
    }), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type your username here'
    }), required=True, help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")

    class Meta:
        """ User Form Meta """
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_first_name(self):
        """ Validate first name """
        first_name = self.cleaned_data.get('first_name')
        if first_name == '':
            self.add_error(
                'first_name',
                forms.ValidationError(
                    'First name is required',
                    code='required'
                )
            )
        return first_name

    def clean_last_name(self):
        """ Validate last name """
        last_name = self.cleaned_data.get('last_name')
        if last_name == '':
            self.add_error(
                'last_name',
                forms.ValidationError(
                    'Last name is required',
                    code='required'
                )
            )
        return last_name

    def clean_email(self):
        """ Validate email """
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            self.add_error(
                'email',
                forms.ValidationError(
                    'This email already exists!'
                )
            )
        return email

    def clean_password_confirmation(self):
        """ Validate password confirmation """
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password and password_confirmation and password != password_confirmation:
            self.add_error(
                'password_confirmation',
                forms.ValidationError(
                    'Passwords do not match',
                    code='password_mismatch'
                )
            )
        return password_confirmation


class UpdateUserForm(forms.ModelForm):
    """
        Update User Form 
    """

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Type your password here'
    }),)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Type your password confirmation here'
    }), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type your first name here',
    }), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type your last name here'
    }), required=True)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Type your email here'
    }), required=True)

    class Meta:
        """ Update User Form Meta """
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        user = super().save(commit=False)

        if password == password_confirmation:
            user.set_password(password)
        if commit:
            user.save()
        return user

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password or password_confirmation:
            if password != password_confirmation:
                self.add_error("password_confirmation",
                               ValidationError("Passwords do not match"))

    def clean_password(self):
        """ Validate password """
        password = self.cleaned_data.get('password')

        if not password:
            return password

        if password:
            try:
                password_validation.validate_password(password)
            except ValidationError as errors:
                self.add_error('password', ValidationError(errors))

    def clean_password_confirmation(self):
        """ Validate password confirmation """
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            self.add_error(
                'password_confirmation',
                forms.ValidationError(
                    'Passwords do not match',
                    code='password_mismatch'
                )
            )
        return password_confirmation

    def clean_email(self):
        """ Validate email """
        current_email = self.instance.email
        email = self.cleaned_data.get('email')
        if current_email == email:
            return email

        exists = User.objects.filter(email=email).exists()
        if exists:
            self.add_error(
                'email',
                forms.ValidationError(
                    'This email already exists!'
                )
            )
        return email
