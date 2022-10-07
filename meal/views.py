from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GroceriesSerializer

from .models import Groceries

# Create your views here.
@api_view(['GET'])
def groceriesList(request):
    groceries = Groceries.objects.all()
    serializer = GroceriesSerializer(groceries, many=True)
    return Response(serializer.data)