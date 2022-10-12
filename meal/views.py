from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoodSerializer

from .models import Food

@api_view(['GET'])
def foodList(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)




