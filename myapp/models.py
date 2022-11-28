from django.db import models

class Greyjoy(models.Model):
    card_num = models.IntegerField(unique=True)
    url = models.CharField(max_length=200)
    used = models.BooleanField()
