# Generated by Django 3.0.7 on 2020-07-05 05:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_remove_image_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='photo',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='photo'),
            preserve_default=False,
        ),
    ]
