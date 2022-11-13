from django.db import models

class Deck(models.Model):
    active = False
    max_size = 20
    starting_hand = 3

class Greyjoy(models.Model):

    # def __init__(self, card_num, url, used):
    #     self.card_num = card_num
    #     self.url = url
    #     self.used = used
    card_num = models.IntegerField(unique=True)
    url = models.CharField(max_length=200)
    used = models.BooleanField()

    # book = Book.create("Pride and Prejudice")
        #super().__init__(card_num, url)

