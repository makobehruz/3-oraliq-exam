from django.db import models
from .base_model import BaseModel
from django.shortcuts import reverse


class Author(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(unique=True)
    phone = models.CharField(max_length=13)
    image = models.ImageField(upload_to='author_image/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_delete_url(self):
        return reverse('authors:delete', args=[self.pk])

