from django.db import models

class Greyjoy(models.Model):
    name = models.CharField(max_length=100)
    card_num = models.IntegerField(unique=True)
    url = models.CharField(max_length=200)
    def __str__(self):
        return 'basic-' + self.name if self.card_num in range(7) else 'commander-' + self.name

class Logo(models.Model):
    faction = models.CharField(max_length= 20, unique=True)
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.faction