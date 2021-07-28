from django.db import models

# Create your models here.


class Collections(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)


class Cards(models.Model):
    answer = models.CharField(max_length=250)
    question = models.CharField(max_length=500)
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE)


