from rest_framework.response import Response
from uritemplate import partial
from .serializers import OrderHistorySerializers
from .models import OrderHistory
from rest_framework.decorators import api_view

@api_view(['GET'])
def getorder(request):
    order=OrderHistory.objects.all()
    serializer=OrderHistorySerializers(order,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updateorder(request):
    data=request.data
    serializer=OrderHistorySerializers(many=True,data=data)
    print(data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)
