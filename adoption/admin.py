from django.contrib import admin

from adoption.models import Interest, Pet

# Register your models here.

admin.site.register(Pet)
admin.site.register(Interest)