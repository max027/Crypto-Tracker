from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer 
from .models import  OrderHistory,Portfolio

class OrderHistorySerializers(ModelSerializer):
    class Meta:
        model=OrderHistory
        fields='__all__'

class PortfolioSerializers(ModelSerializer):
    class Meta:
        model=Portfolio
        fields='__all__'