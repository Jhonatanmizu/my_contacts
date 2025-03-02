"""
 Contact models
"""
from django.db import models  # type: ignore
from django.utils import timezone  # type: ignore


class Contact(models.Model):
    """ 
    Contact model
    """
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=True)
    picture = models.ImageField(
        blank=True, null=True, upload_to='pictures/contacts/%Y/%m/')

    def __str__(self):
        return f'{self.name} / {self.email} / {self.phone_number}'
