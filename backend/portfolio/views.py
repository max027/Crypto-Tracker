import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderHistorySerializers
from .models import OrderHistory

class GetOrder(APIView):
    def get(self,request,format=None):
        order=OrderHistory.objects.all()
        serializer=OrderHistorySerializers(order,many=True)
        Response(serializer.data)