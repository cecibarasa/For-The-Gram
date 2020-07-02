from django.db import models

# Create your models here.
class Instalite(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_lenght=30)
    email = models.EmailField()