from django.db import models

class emp(models.Model):
    ename = models.CharField(max_length=250)
    esal = models.IntegerField()
    email = models.EmailField(max_length=250)

class User(models.Model):
    Empnm = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    password = models.IntegerField()