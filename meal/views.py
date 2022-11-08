from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import FoodData


def index(request):
    return render(request, 'meal/index.html')

def bmi(request):
    context = {}
    weight = request.GET.get('bmi_weight')
    height = request.GET.get("bmi_height")
    if height and weight is not None:
        height_to_meter = int(height)/100
        resultOfBMI = round(int(weight)/(height_to_meter**2), 2)
        context.update({
            "result" : resultOfBMI,
            "height" : height,
            "weight" : weight,
        })
    return render(request, 'meal/bmi.html', context)

def food_Database(request):
    page = request.GET.get("page", 1) 
    food_records = FoodData.objects.all()
    divide_pages = Paginator(food_records, 10)
    page_format = divide_pages.get_page(page)
    context = {
        "foodlist": page_format
    }
    return render(request, 'meal/database.html', context)



