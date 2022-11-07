from django.shortcuts import render, redirect
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



