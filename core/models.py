from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=222)
    firstname = models.CharField(max_length=111)
    age = models.IntegerField()