# Generated by Django 5.1.5 on 2025-02-02 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_author_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='created_at',
            new_name='create_at',
        ),
    ]
