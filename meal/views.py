from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoodSerializer

from .models import FoodDB

@api_view(['GET'])
def foodList(request):
    food = FoodDB.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)




