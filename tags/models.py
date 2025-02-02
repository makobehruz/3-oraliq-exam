from django.db import models
from authors.base_model import BaseModel
from django.shortcuts import reverse


class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_delete_url(self):
        return reverse('tags:delete', args=[self.pk])