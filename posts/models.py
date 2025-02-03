from django.db import models
from authors.base_model import BaseModel
from authors.models import Author
from catalogs.models import Category
from tags.models import Tag
from django.shortcuts import reverse
from django.utils.text import slugify


class Post(BaseModel):
    name = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts_image/')
    desc = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('posts:detail', args=[
            self.pk,
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name

