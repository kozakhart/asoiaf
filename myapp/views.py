from django.shortcuts import render
from .models import Greyjoy

def home(request):
    create = create_cards()
    print(Greyjoy.objects.filter(card_num=1).values_list('url'))  
    return  render(request, 'home.html', {'deck':create})


def create_cards():
    counter = 0
    all_objects = Greyjoy.objects.all()
    if len(all_objects) == 14:
        print('works')
    else:
        for x in range(2):
            for num in range(7):
                counter += 1
                url = greyjoy_cards(num)
                greyjoy = Greyjoy.objects.create(card_num=counter, url=url, used=False)
                greyjoy.save()
                Greyjoy.url = url
                Greyjoy.used = False

    deck = []
    for card in all_objects:
        deck.append(card.url)
        print(card.url)
    return deck

def greyjoy_cards(url):
    basic_cards = {
    'bless-with-stone-bless-with-steel': 'https://asoiaf-app.s3.us-west-1.amazona`ws.com/bless-with-stone-bless-with-steel.jpg',
    'raiding-call': 'https://asoiaf-app.s3.us-west-1.amazonaws.com/raiding-call.jpg', 
    'finger-dance': 'https://asoiaf-app.s3.us-west-1.amazonaws.com/finger-dance.jpg', 
    'the-iron-price': 'https://asoiaf-app.s3.us-west-1.amazonaws.com/the-iron-price.jpg',
    'the-krakens-wrath': 'https://asoiaf-app.s3.us-west-1.amazonaws.com/the-krakens-wrath.jpg',
    'what-is-dead-may-never-die': 'https://asoiaf-app.s3.us-west-1.amazonaws.com/what-is-dead-may-never-die.jpg',
    'we-do-not-sow': 'https://asoiaf-app.s3.us-west-1.amazonaws.com/we-do-not-sow.jpg'
    }
    return list(basic_cards.values())[url]

def logos(faction):
    logos = {
    'greyjoy': 'https://asoiaf-app.s3.us-west-1.amazonaws.com/greyjoy-logo.png'
    }
