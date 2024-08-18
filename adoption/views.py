from django.http import HttpResponse
from django.shortcuts import render

from adoption.models import Pet

# Create your views here.

def index(request):
    pets = Pet.objects.all()
    context={
        'pets':pets
    }
    return render(request, 'adoption/index.html', context)

def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    
    context = {
        'pet':pet,
    }
    return render(request, 'adoption/pet_detail.html', context)