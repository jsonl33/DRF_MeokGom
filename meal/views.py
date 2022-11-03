from django.shortcuts import render
from .models import FoodData

def index(request):
    return render(request, 'meal/index.html')




