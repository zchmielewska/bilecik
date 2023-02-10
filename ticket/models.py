from django.db import models


class Model(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    model = models.ManyToManyField(Model)
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    version = models.CharField(max_length=128)
