from django.urls import path
from . import views

app_name="meal"
urlpatterns = [
    path('groceries-list/', views.groceriesList, name="groceries-list")
]
