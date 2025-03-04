"""
 Contact models
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User

class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        """Category model metadata"""
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f'{self.name}'


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
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f'{self.name} / {self.email} / {self.phone_number}'
