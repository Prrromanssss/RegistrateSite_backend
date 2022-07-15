from django.db import models


class Registrate(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    surname = models.CharField(max_length=150, verbose_name='Surname')
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=246)
    password = models.CharField(max_length=150, verbose_name='Password')

