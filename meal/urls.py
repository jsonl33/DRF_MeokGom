from django.urls import path
from . import views

app_name="meal"
urlpatterns = [
    path('food-list/', views.foodList, name="food-list")
]
