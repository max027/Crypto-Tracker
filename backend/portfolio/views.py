from rest_framework.response import Response
from .serializers import OrderHistorySerializers,PortfolioSerializers
from .models import OrderHistory,Portfolio
from rest_framework.decorators import api_view

@api_view(['GET'])
def getorder(request):
    order=OrderHistory.objects.all()
    serializer=OrderHistorySerializers(order,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updateorder(request):
    data=request.data
    serializer=OrderHistorySerializers(data=data)
    if serializer.is_valid():
        serializer.save()
    print(serializer.errors) 
    return Response(serializer.data)

@api_view(['GET'])
def getportfolio(request):
    portfolio=Portfolio.objects.all()
    serializer=PortfolioSerializers(portfolio,many=True)
    return Response(serializer.data)

@api_view(['PUT','POST'])
def updateportfolio(request):
    data=request.data
    serializer=PortfolioSerializers(data=data)
    name=data
    if serializer.is_valid():
        if Portfolio.objects.filter(coin_name=name['coin_name']):
            total=name['order_price']
            print(total)
        else:
            serializer.save()        

    return Response(serializer.data)