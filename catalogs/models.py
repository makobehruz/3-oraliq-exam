from django.db import models
from authors.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
