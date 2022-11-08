from django.urls import path
from . import views

app_name="meal"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('bmi/', views.bmi, name="bmi"),
    path('database/', views.food_Database, name="database"),
]
