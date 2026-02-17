from django.db import models

# Create your models here.
class Startup(models.Model):
    u_name = models.CharField(max_length=30)