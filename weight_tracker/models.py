from django.db import models


class Weight(models.Model):
    value = models.IntegerField()
    date = models.DateField(auto_now=True)
