from django.contrib import admin
from .models import *


class GreyjoyAdmin(admin.ModelAdmin):
    search_fields=['name', 'card_num']
    model = Greyjoy

admin.site.register(Greyjoy, GreyjoyAdmin)
admin.site.register(Logo)