from django.db import models

class Aula(models.Model):
    name = models.CharField(max_length=255)