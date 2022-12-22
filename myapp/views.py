from django.shortcuts import render
from .models import *
from django.template.response import TemplateResponse

from django.http import HttpResponse
from django.template import loader

def home(request):

    logos = Logo.objects.all()
    greyjoy = Greyjoy.objects.all()

    template = loader.get_template('home.html')
    context = {
    'logos': logos,
    'greyjoy': greyjoy,
    }
    return HttpResponse(template.render(context, request))

def create_logos():
    #clear urls
    Logo.objects.all().delete()

    faction_list = ['Lannister', 'Stark', 'Free-Folk', 'Neutral', 'Nights-Watch', 'Baratheon', 'Targaryen', 'Greyjoy', 'Martell']
    
    iterator = 0
    for fac in faction_list:
        print(fac)
        faction_list[iterator] = Logo()
        faction_list[iterator].faction = fac
        faction_list[iterator].save()
        iterator += 1

def greyjoy_cards():
    Greyjoy.objects.all().delete()

    card_list = [
    'bless-with-stone-bless-with-steel',
    'raiding-call', 
    'finger-dance', 
    'the-iron-price',
    'the-krakens-wrath',
    'what-is-dead-may-never-die',
    'we-do-not-sow'
    ]

    commander_list = [
    'euron-cunning-ploy',
    'euron-devious-methods',
    'euron-mind-games',
    'victarion-assault-orders',
    'victarion-rush-of-aggression',
    'victarion-sustained-assault'
    ]

    card_count = 0
    for card in card_list:
        print(card)
        card_list[card_count] = Greyjoy()
        card_list[card_count].name = card
        card_list[card_count].card_num = card_count
        card_list[card_count].__str__()
        card_list[card_count].save()
        card_count += 1

    iterator = 0
    for card in commander_list:
        print(card)
        commander_list[iterator] = Greyjoy()
        commander_list[iterator].name = card
        commander_list[iterator].card_num = card_count
        commander_list[iterator].__str__()
        commander_list[iterator].save()
        iterator, card_count = iterator + 1, card_count + 1
#DO NOT RUN
#create_logos()
#greyjoy_cards()