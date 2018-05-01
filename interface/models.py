from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=70)
    username = models.CharField(max_length=32, unique=True)
    phn_numb = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
