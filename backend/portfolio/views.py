from rest_framework.response import Response
from .serializers import OrderHistorySerializers
from .models import OrderHistory
from rest_framework.decorators import api_view

@api_view(['GET'])
def getorder(request):
    order=OrderHistory.objects.all()
    serializer=OrderHistorySerializers(order,many=True)
    return Response(serializer.data)